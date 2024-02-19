import tkinter as tk
from tkinter import messagebox
from utils import *
from pages import *
from cryptography.fernet import Fernet
import os
root = tk.Tk()

# Setting the window size
root.geometry("400x300")
root.title("Login System")
root.iconbitmap("Img/favicon.ico")

# Styling
root.configure(bg="#EFEFEF")

user_var = tk.StringVar()
passw_var = tk.StringVar()

# Storing all
def main():
    
    def submit():
        if passw_var.get() == "" or user_var.get() == "":
            messagebox.showwarning(
                "Empty Fields", "Please enter both username and password."
            )
            return False
        
        password_manager = PasswordManager(passw_var.get())
        # Check if the website is already present
        credentials = password_manager.get_credential("Locked.com")
        
        if credentials is None:
            # If no credentials are found, add a new credential
            password_manager.add_credential("Locked.com", user_var.get(), passw_var.get())
            print("Credential added successfully.")
        else:
            # If credentials are found, check if the entered credentials match
            
            if credentials["username"] == user_var.get() and credentials["password"] == passw_var.get():
                print("Success: Credentials match.")
            else:
                print("Error: Credentials do not match.")
        print(credentials)
        # Reset the entry fields
        passw_var.set("")
        user_var.set("")

    # UI Components
    title_label = tk.Label(
        root, text="Login System", font=("Helvetica", 20, "bold"), bg="#EFEFEF"
    )
    name_label = tk.Label(root, text="Username", font=("Helvetica", 12), bg="#EFEFEF")
    name_entry = tk.Entry(root, textvariable=user_var, font=("Helvetica", 12))
    passw_label = tk.Label(root, text="Password", font=("Helvetica", 12), bg="#EFEFEF")
    passw_entry = tk.Entry(
        root, textvariable=passw_var, font=("Helvetica", 12), show="*"
    )
    sub_btn = tk.Button(
        root,
        text="Submit",
        command=submit,
        font=("Helvetica", 12),
        bg="#4CAF50",
        fg="white",
    )
    

    # Layout
    title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))
    name_label.grid(row=1, column=0, pady=(10, 5))
    name_entry.grid(row=1, column=1, pady=(10, 5))
    passw_label.grid(row=2, column=0, pady=5)
    passw_entry.grid(row=2, column=1, pady=5)
    sub_btn.grid(row=3, column=1, pady=20)
    

    root.mainloop()


if __name__ == "__main__":
    main()
