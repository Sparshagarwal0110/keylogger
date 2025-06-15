# 🔐 Encrypted Keylogger with Log Decryption Tool

A **proof-of-concept (PoC)** Python project demonstrating a secure keylogger with encrypted logging, optional local data exfiltration, and a decryption utility.

> ⚠️ **Strictly for educational and cybersecurity awareness purposes only.**

---

## ⚠️ Disclaimer

This project is intended **only for ethical hacking, educational, or research use**.

- ❌ **Do NOT** use this software on devices you do not own or without explicit consent.
- ⚠️ Unauthorized use may violate privacy laws and ethical standards.

---

## 📦 Requirements

- Python 3.7 or higher
- Install dependencies:

```bash
pip install cryptography pynput
```

---

## 🚀 Getting Started

### 1️⃣ Start the Local Server (Optional)

Simulate data exfiltration to a local server:

```bash
python keylogger.py --server
```

### 2️⃣ Run the Keylogger

```bash
python keylogger.py
```

- Starts capturing and encrypting keystrokes.
- Press `ESC` to stop.
- Encrypted logs are saved to `keylog.enc`.

### 3️⃣ Decrypt the Logs

```bash
python decrypt.py
```

- Decrypted logs are saved to `decrypted_keylogs.txt`.

---

## 🔍 How It Works

- A **Fernet symmetric key** is generated on first run and saved to `secret.key`.
- Logged keystrokes are timestamped, encrypted, and saved in `keylog.enc`.
- Optionally, encrypted logs are sent to a local socket server at `127.0.0.1:5000`.
- The `decrypt.py` script reads and decrypts the logs using the same key.

---

## ✅ Features

- 🔐 AES-128-based encryption with `cryptography.Fernet`
- ⏱️ Timestamped logging
- 📤 Optional local exfiltration via sockets
- 🛑 `ESC` key to safely stop logging
- 📂 Decryption script included

---

## 🧠 For Researchers & Educators

Use this tool to:

- Understand encrypted logging mechanisms
- Simulate malware behavior in a lab environment
- Learn about basic cybersecurity and ethical hacking techniques

---

## 📄 License

MIT License  
© 2025 Sparsh Agarwal

---

## 🙋‍♂️ Contact

Have suggestions, improvements, or questions?  
Feel free to open an issue or submit a pull request.
