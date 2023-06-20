import tkinter as tk
from tkinter import ttk


count = 0

def clicked1():
    global count

    count = count + 1

    label1.configure(text=f'Button has been clicked {count} times.')


windows = tk.Tk()
windows.title("Clicker Counter:")

label = tk.Label(windows, text="Click this cos why not ➜")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="Click Here!", command=clicked1)
custom_button.grid(column=1, row=0)

count2 = 0

def clicked2():
    global count2

    count2 = count2 + 1

    label2.configure(text=f'Button has been clicked {count2} times.')

label = tk.Label(windows, text="Click this cos why not ➜" )
label.grid(column=0, row=2)

label2 = tk.Label(windows)
label2.grid(column=0, row=3)

custom_button = ttk.Button (windows, text="Click Here!", command=clicked2 )
custom_button.grid(column=1, row=2)



windows.mainloop()