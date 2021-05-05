from tkinter import *
from tkinter import ttk

class InfoWindow:
    def __init__(self, master, title, text_or_file, file=False):
        window = Toplevel(master)
        window.title(title)
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)

        s = ttk.Sizegrip(window)
        s.grid(column=1, row=1, sticky=(S,E))
        
        text = text_or_file
        if file:
            with open(text_or_file, 'r') as f:
                text = f.read()

        s = ttk.Style()
        s.configure('Label1.TLabel', background="white")
            
        label = ttk.Label(window, text=text, anchor=W, style='Label1.TLabel')
        label.grid(row=0, column=0, padx=10, pady=10, sticky=(N,S,E,W))
