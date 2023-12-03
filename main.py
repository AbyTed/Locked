import tkinter as tk
from tkinter import ttk
window = tk.Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# widgets
l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

entry = tk.Entry(width=20,height=5)
entry.pack()

name = entry.get()
print(name)

# packing
l2.pack()
l1.pack()
# testing
print('working')
window.mainloop()

