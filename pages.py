from utils import *


def main_page(root, name_var, passw_var, tk):
    website_var = tk.StringVar()

    def add():
        # data -> show on screen and saved temp
        UserNewCredentials = StoredCredential(
            passw_var.get(), name_var.get(), website_var.get()
        )
        # encryption

        # data -> database
        passw_var.set("")
        name_var.set("")
        website_var.set("")
        pass

    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text="add User", font=("calibre", 10, "bold"))

    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root, textvariable=name_var, font=("calibre", 10, "normal"))

    # creating a label for password
    passw_label = tk.Label(root, text="add Password", font=("calibre", 10, "bold"))

    # creating a entry for password
    passw_entry = tk.Entry(
        root, textvariable=passw_var, font=("calibre", 10, "normal"), show="*"
    )
    website_label = tk.Label(root, text="add website", font=("calibre", 10, "bold"))

    website_entry = tk.Entry(
        root, textvariable=website_var, font=("calibre", 10, "normal")
    )

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(root, text="Submit", command=add)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    website_label.grid(row=2, column=0)
    website_entry.grid(row=2, column=1)
    sub_btn.grid(row=3, column=1)
