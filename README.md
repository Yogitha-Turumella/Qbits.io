# **QBits: Quantum Encryption Demo**

## **🔹 Introduction**
**QBits** is a **Quantum Key Distribution (QKD) demo** built using **Flask and Qiskit**, demonstrating how quantum cryptography enhances security beyond classical encryption algorithms like **AES** and **RSA**. This project highlights how **Quantum Bits (Qubits)** can provide **unbreakable encryption** through the **BB84 protocol**.

---

## **🔹 Features**
✅ **Quantum Key Distribution (BB84 Protocol)**
✅ **Secure Key Exchange Using Qubits**
✅ **Tamper Detection & Eavesdropping Alerts**
✅ **Quantum Random Number Generation (QRNG)**
✅ **Flask-Based Web Interface for Encryption Demo**

---

## **🔹 Quantum Cryptography vs Classical Cryptography**
| Feature          | AES-256 / RSA-2048       | QKD (BB84 - QBits.io) |
|-----------------|-------------------------|-----------------------|
| **Security Based On** | Mathematical complexity | Quantum mechanics |
| **Vulnerability to Quantum Attacks** | Breakable by **Shor’s Algorithm** (RSA) and **Grover’s Algorithm** (AES) | **Unbreakable** due to Heisenberg’s Uncertainty Principle |
| **Eavesdropping Detection** | **No in-built detection** | **Instant detection** if an attacker tries to intercept the key |
| **Longevity of Security** | **Vulnerable in the post-quantum era** | **Future-proof and quantum-safe** |

🚀 **QBits.io demonstrates the future of encryption—one that remains secure even against quantum computers!**

---

## **🔹 Quantum Concepts Used in QBits.io**

### **1️⃣ Quantum Key Distribution (QKD) – BB84 Protocol**  
The **BB84 protocol** ensures that encryption keys are securely exchanged between parties. Unlike classical key exchange methods, it prevents eavesdropping by leveraging:
- **Quantum Superposition**: Qubits exist in multiple states until measured, making interception impossible.
- **Quantum Measurement & No-Cloning Theorem**: Any attempt to measure qubits changes their state, revealing attackers.

### **2️⃣ Quantum Random Number Generation (QRNG)**
Traditional encryption relies on **pseudo-random numbers**, which can be predictable. Quantum-generated numbers are **truly random**, making encryption more secure.

---

## **🔹 Installation and Setup**
### **🔧 Prerequisites**
- Python 3.8+
- Flask
- Qiskit
- Git

### **📌 Steps to Run QBits.io**
1️⃣ Clone the repository:
```sh
 git clone https://github.com/Yogitha-Turumella/QBits.io.git
 cd QBits.io
```
2️⃣ Install dependencies:
```sh
 pip install -r requirements.txt
```
3️⃣ Run the Flask server:
```sh
 python app.py
```
4️⃣ Open **http://127.0.0.1:5000/** in your browser.

---

## **🔹 Project Screenshots**
![Quantum Key Distribution](screenshotss/output1.png)
![Secure Communication](screenshotss/output2.png)

---

## **🔹 Contribution**
Feel free to fork this repository, raise issues, and submit pull requests to improve the project.

---

🚀 **Explore the power of Quantum Cryptography with QBits.io!** 🔐

