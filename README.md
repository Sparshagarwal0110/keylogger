🔐 Encrypted Keylogger with Log Decryption Tool
A proof-of-concept (PoC) project demonstrating an encrypted keylogger written in Python with optional local data exfiltration and a decryption script.
Strictly for educational and cybersecurity awareness purposes.

⚠️ DISCLAIMER
This project is intended solely for educational, ethical hacking, or cybersecurity research purposes.
Do not use this software to monitor or log keystrokes on devices you do not own or without clear, informed consent.
Misuse of this tool can be illegal and unethical.

🔧 Requirements
Python 3.7+

Install dependencies:


pip install cryptography pynput
🚀 How to Use
🔹 1. Start the Local Server (Optional)
Simulates exfiltration of encrypted keystroke data:


python keylogger.py --server
🔹 2. Run the Keylogger

python keylogger.py
Logs all keystrokes and encrypts them using cryptography.Fernet.

Press ESC to stop the keylogger.

Encrypted logs are saved to keylog.enc.

🔹 3. Decrypt the Logs

python decrypt.py
Decrypted output is saved to decrypted_keylogs.txt.

🔐 How It Works
A Fernet symmetric encryption key is generated and saved in secret.key.

Each log entry (timestamp + keys) is encrypted and stored in keylog.enc.

Optionally, the logs are sent to a local server over a socket connection.

The decrypt.py script decrypts the logs back into plaintext.

📌 Features
🔐 Strong encryption with cryptography.Fernet

📅 Timestamps for each log entry

📤 Optional socket-based exfiltration to localhost

🛑 ESC key kill switch

💾 Log decryption utility included

📎 For Researchers & Educators
This project can be used to:

Understand secure logging and encryption techniques

Study ethical keylogging and forensics in a controlled environment

Demonstrate basic concepts of data exfiltration for red teaming simulations

📄 License
MIT License
© 2025 Sparsh Agarwal

✉️ Contact
Feel free to open an issue or submit a pull request for suggestions or contributions.
