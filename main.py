import tkinter as tk
import json
from defined  import *
from page import *

root=tk.Tk()

# setting the windows size
root.geometry("600x400")

root.title('Locked')


root.iconbitmap("favicon.ico")


pop_up_bool = False
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
FirstUser = Credential('','')
# new label storage


# defining a function that will
# get the name and password and 
# print them on the screen
def submit():
    FirstUser.Username = name_var.get()
    FirstUser.Password = passw_var.get()

    passw_var.set("")
    name_var.set("")
    if FirstUser.Username == 'A' and FirstUser.Password == 'T':
        main_page(root, name_var, passw_var,tk)

       
	
# creating a label for 
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
# creating  a popup warning
# label
pop_up = tk.Label(root, text = 'Please Enter Valid Credential', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# sign up button


# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
# performing an infinite loop 
# for the window to display
root.mainloop()

