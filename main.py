import json
import tkinter as tk
from utils import *
from pages import *

root = tk.Tk()

# setting the windows size
root.geometry("800x400")

root.title("Locked")


root.iconbitmap("Img/favicon.ico")


pop_up_bool = False
# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()
FirstUser = Credential("", "")


# storing all
def main():
    def submit():
        FirstUser.Username = name_var.get()
        FirstUser.Password = passw_var.get()

        with open("store.json", "r") as open_file:
            # Reading from json file
            json_object = json.load(open_file)
        passw_var.set("")
        name_var.set("")
        if (
            FirstUser.Username == json_object["user"]
            and FirstUser.Password == json_object["password"]
        ):
            main_page(root, name_var, passw_var, tk)

    # signing up by using existing entries
    def sign_up():
        FirstUser.Username = name_var.get()
        FirstUser.Password = passw_var.get()

        json_credentials = {"user": FirstUser.Username, "password": FirstUser.Password}
        with open("store.json", "w") as outfile:
            json.dump(json_credentials, outfile, indent=2)

    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text="Username", font=("calibre", 10, "bold"))
    # creating  a popup warning
    # label
    pop_up = tk.Label(
        root,
        text="Please Enter Valid Credentials \n if you like to sign up please put in credentials \n 1. type your user and password you want \n 2. click sign up \n 3. you then can now input your user and password you have just created",
        font=("calibre", 10, "bold"),
    )

    # creating a entry for input name
    name_entry = tk.Entry(root, textvariable=name_var, font=("calibre", 10, "normal"))

    # creating a label for password
    passw_label = tk.Label(root, text="Password", font=("calibre", 10, "bold"))

    # creating a entry for password
    passw_entry = tk.Entry(
        root, textvariable=passw_var, font=("calibre", 10, "normal"), show="*"
    )

    # creating a button using the widget -> submit()
    sub_btn = tk.Button(root, text="Submit", command=submit)

    # sign up button

    sign_up = tk.Button(root, text="Sign Up", command=sign_up)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)
    sign_up.grid(row=2, column=0)
    pop_up.grid(row=0, column=8)
    # performing an infinite loop
    # for the window to display
    root.mainloop()


if __name__ == "__main__":
    main()
