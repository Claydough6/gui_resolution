from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0

def click(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def drawLine(event):
    global lastx, lasty
    canvas.create_line(lastx, lasty, event.x, event.y, fill="red")
    lastx, lasty = event.x, event.y

# create the root window
root = Tk()
root.title("Canvas Window")
root.option_add('*tearOff', FALSE)  # so the menu doesn't look weird

# create the canvas
canvas = Canvas(root)

# bind the commands
canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", drawLine)

# populate the grid
canvas.grid()

# run the app
root.mainloop()
