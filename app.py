from flask import Flask, render_template, request, jsonify
import random
import base64
import hashlib
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from cryptography.fernet import Fernet

app = Flask(__name__)

# Quantum Key Distribution (QKD) Simulation
def generate_quantum_key(num_bits=10, eavesdrop=False):
    alice_bits = [random.randint(0, 1) for _ in range(num_bits)]
    alice_bases = [random.choice(['+', 'X']) for _ in range(num_bits)]

    simulator = AerSimulator()
    bob_bases = [random.choice(['+', 'X']) for _ in range(num_bits)]
    bob_bits = []

    for bit, base, bob_base in zip(alice_bits, alice_bases, bob_bases):
        qc = QuantumCircuit(1, 1)
        if bit:
            qc.x(0)
        if base == 'X':
            qc.h(0)
        if bob_base == 'X':
            qc.h(0)
        qc.measure(0, 0)
        qc = transpile(qc, simulator)
        result = simulator.run(qc, shots=1).result()
        measured_bit = int(list(result.get_counts().keys())[0])
        bob_bits.append(measured_bit)

    if eavesdrop:
        bob_bits = [random.randint(0, 1) if random.random() < 0.3 else bit for bit in bob_bits]

    final_key = ''.join(str(bob_bits[i]) for i in range(num_bits) if alice_bases[i] == bob_bases[i])
    return final_key[:16]

# Encrypt a message using QKD key
def encrypt_message(message, key):
    try:
        hashed_key = hashlib.sha256(key.encode()).digest()[:32]
        cipher = Fernet(base64.urlsafe_b64encode(hashed_key))
        encrypted_message = cipher.encrypt(message.encode()).decode()
        return encrypted_message
    except Exception as e:
        return str(e)

# Decrypt a message using QKD key
def decrypt_message(encrypted_message, key):
    try:
        hashed_key = hashlib.sha256(key.encode()).digest()
        fernet_key = base64.urlsafe_b64encode(hashed_key[:32])  # Ensuring valid length
        
        cipher = Fernet(fernet_key)
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except Exception as e:
        return f"Decryption Error: {str(e)}"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/encrypt_page')
def encrypt_page():
    return render_template("encrypt_page.html")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        message = data.get("message", "")
        eavesdrop = data.get("eavesdrop", False)

        if not message:
            return jsonify({"error": "No message provided"}), 400

        qkd_key = generate_quantum_key(num_bits=10, eavesdrop=eavesdrop)
        encrypted_message = encrypt_message(message, qkd_key)

        return jsonify({"qkd_key": qkd_key, "encrypted_message": encrypted_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        encrypted_message = data.get("encrypted_message", "")
        qkd_key = data.get("qkd_key", "")

        if not encrypted_message or not qkd_key:
            return jsonify({"error": "Missing encrypted message or key"}), 400

        decrypted_message = decrypt_message(encrypted_message, qkd_key)
        return jsonify({"decrypted_message": decrypted_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
