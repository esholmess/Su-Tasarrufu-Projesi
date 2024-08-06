import tkinter as tk

def pad(num):
    return num

root = tk.Tk()

root.geometry("300x300")
label = tk.Label(root, text=pad(9)).pack()

root.mainloop()