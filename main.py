import json
import tkinter as tk
from tkinter import messagebox
from utils import *
from pages import *
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key_from_password(password, salt=b'244'):
    # Derive a key from the user-provided password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations for security
        salt=salt,
        length=32  # Length of the derived key
    )

    key = kdf.derive(password.encode())
    return key

def encrypt_data(key, plaintext):
    cipher_suite = Fernet(key.encode())
    encrypted_text = cipher_suite.encrypt(plaintext.encode())
    return encrypted_text

def decrypt_data(key, ciphertext):
    cipher_suite = Fernet(base64.urlsafe_b64decode(key))
    decrypted_text = cipher_suite.decrypt(ciphertext).decode()
    return decrypted_text

def check_master_password(name_var, passw_var):
    # Derive the key from the username
    key = generate_key_from_password(name_var.get())
    
    # Encrypt the entered password with the derived key
    entered_password_encrypted = encrypt_data(key, passw_var.get())

    # Convert the encrypted entered password to a string for comparison
    entered_password_str = base64.b64encode(entered_password_encrypted).decode()

    # Retrieve the stored hashed password from the JSON file
    with open("store.json", "r") as outfile:
        stored_credentials = json.load(outfile)

    stored_password_str = stored_credentials.get("passwordLocked", "")

    # Compare the stored hashed password with the derived key from the entered password
    return entered_password_str == stored_password_str


root = tk.Tk()

# Setting the window size
root.geometry("400x300")
root.title("Login System")
root.iconbitmap("Img/favicon.ico")

# Styling
root.configure(bg="#EFEFEF")

name_var = tk.StringVar()
passw_var = tk.StringVar()
FirstUser = Credential("", "")

# Storing all
def main():

    def submit():
        
            
        passw_var.set("")
        name_var.set("")
        
        check_login = check_master_password(name_var, passw_var)
        if (check_login):
            PasswordPage(any, name_var.get(), any, any)
            print('f')
            
            pass

    def sign_up():
        if passw_var.get() == "" or passw_var.get() == "":
            messagebox.showwarning("Empty Fields", "Please enter both username and password.")
            return False
        key = generate_key_from_password(name_var.get())
        
        FirstUser.Password = encrypt_data(key, passw_var.get())
        

        password_str = base64.b64encode(FirstUser.Password).decode()
        
        json_credentials = {"userLocked": name_var.get(), "passwordLocked": password_str}

        with open("store.json", "w") as outfile:
            json.dump(json_credentials, outfile, indent=2)

    # UI Components
    title_label = tk.Label(root, text="Login System", font=("Helvetica", 20, "bold"), bg="#EFEFEF")
    name_label = tk.Label(root, text="Username", font=("Helvetica", 12), bg="#EFEFEF")
    name_entry = tk.Entry(root, textvariable=name_var, font=("Helvetica", 12))
    passw_label = tk.Label(root, text="Password", font=("Helvetica", 12), bg="#EFEFEF")
    passw_entry = tk.Entry(root, textvariable=passw_var, font=("Helvetica", 12), show="*")
    sub_btn = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12), bg='#4CAF50', fg='white')
    sign_up_btn = tk.Button(root, text="Sign Up", command=sign_up, font=("Helvetica", 12), bg='#2196F3', fg='white')

    # Layout
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))
    name_label.grid(row=1, column=0, pady=(10, 5))
    name_entry.grid(row=1, column=1, pady=(10, 5))
    passw_label.grid(row=2, column=0, pady=5)
    passw_entry.grid(row=2, column=1, pady=5)
    sub_btn.grid(row=3, column=1, pady=20)
    sign_up_btn.grid(row=3, column=0, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
 
