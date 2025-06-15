import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
LOG_FILE = "keylog.enc"
OUTPUT_FILE = "decrypted_keylogs.txt"

def load_key():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(f"Key file '{KEY_FILE}' not found.")
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def decrypt_log_and_save():
    key = load_key()
    fernet = Fernet(key)

    if not os.path.exists(LOG_FILE):
        raise FileNotFoundError(f"Log file '{LOG_FILE}' not found.")

    with open(LOG_FILE, 'rb') as f:
        lines = f.readlines()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_file:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                decrypted = fernet.decrypt(line).decode()
                out_file.write(decrypted + '\n')
            except Exception as e:
                out_file.write(f"[!] Failed to decrypt a line: {e}\n")

    print(f"[*] Decrypted logs saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    decrypt_log_and_save()
