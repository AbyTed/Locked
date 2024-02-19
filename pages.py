from utils import *


import tkinter as tk

class PasswordPage(tk.Frame):
    def __init__(self, parent, master_password, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.master_password = master_password

        label = tk.Label(self, text="Welcome to the Password Page!", font=("Helvetica", 16))
        label.pack(pady=10)

        # Create a button to retrieve and display passwords
        show_passwords_button = tk.Button(self, text="Show Passwords", command=self.show_passwords)
        show_passwords_button.pack(pady=10)

    def show_passwords(self):
        print("Displaying passwords...")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Password Manager")

    # Assume you have a master password entered by the user
    master_password = "user_entered_master_password"

    # Create and show the main page
    main_page = PasswordPage(root, master_password)
    main_page.pack(expand=True, fill="both")

    root.mainloop()
