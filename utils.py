import json
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, master_password, storage_file="passwords.json"):
        self.master_key = self.generate_key_from_password(master_password)
        self.fernet_instance = Fernet(self.master_key)
        self.storage_file = storage_file
        self.credentials = self.load_credentials()

    def generate_key_from_password(self, password, salt=b"244"):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt_data(self, plaintext):
        encrypted_text = self.fernet_instance.encrypt(plaintext.encode())
        print(self.decrypt_data(encrypted_text))
        print(self.master_key)
        return encrypted_text

    def decrypt_data(self, ciphertext):
        try:
            decrypted_text = self.fernet_instance.decrypt(ciphertext).decode()
            return decrypted_text
        except Exception as e:
            print(f"Error decrypting data: {e}")
            return None

    def load_credentials(self):
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_credentials(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.credentials, file, indent=2)

    def add_credential(self, website, username, password):
        encrypted_username = self.encrypt_data(username)
        encrypted_password = self.encrypt_data(password)
        print(encrypted_password, "\n", encrypted_username)
        self.credentials[website] = {
            "username": base64.b64encode(encrypted_username).decode(),
            "password": base64.b64encode(encrypted_password).decode(),
        }
        self.save_credentials()

    def get_credential(self, website):
        # Retrieve the stored credentials from the JSON file
        stored_credentials = self.load_credentials()

        # Check if the website is present in the stored credentials
        if website in stored_credentials:
            credential_data = stored_credentials[website]

            # Decode the base64-encoded username and password before decryption
            encrypted_username = base64.b64decode(credential_data["username"])
            encrypted_password = base64.b64decode(credential_data["password"])

            # Decrypt the stored username and password using the master key
            decrypted_username = self.decrypt_data(encrypted_username)
            decrypted_password = self.decrypt_data(encrypted_password)

            # Return the decrypted username and password along with other credential information
            return {
                'username': decrypted_username,
                'password': decrypted_password,
                'website': website
            }
        else:
            # Return None if the website is not found
            return None
    




