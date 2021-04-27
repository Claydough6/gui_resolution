from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

lastx, lasty = 0, 0

def click(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def drawLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line(lastx, lasty, x, y, fill="red")
    lastx, lasty = x, y

# create the root window (themed now!)
root = ThemedTk(theme="breeze")
root.title("Canvas Window")
root.option_add('*tearOff', FALSE)  # so the menu doesn't look weird

# create frame to put canvas
frame = ttk.Labelframe(root, text="Draw:")

# create the canvas
canvas = Canvas(frame)
canvas.config(scrollregion=(0,0,1000,1000))
canvas.configure(bg='white')

# create scrollbars
sx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
sy = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
canvas.configure(xscrollcommand=sx.set)
canvas.configure(yscrollcommand=sy.set)

# bind the commands
canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", drawLine)

# populate the grid
frame.grid(padx=10, pady=10)
canvas.grid(column=0, row=0)
sx.grid(column=0, row=1, sticky=(E,W))
sy.grid(column=1, row=0, sticky=(N,S))

# create the sizegrip
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(S,E))

# edit the scaling
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(999, weight=1)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(999, weight=1)

# run the app
root.mainloop()
