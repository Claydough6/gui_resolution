from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

from resolution_canvas import ResolutionCanvas
from statement_frame import StatementFrame

__version__ = 0.3

# create the root window
root = ThemedTk()
root.title("Graphical Resolution " + str(__version__))
root.option_add('*tearOff', FALSE)  # so the menu doesn't tear

# used to display the help menu
def getHelp(*args):
    help_window = Toplevel(root)
    help_window.title("Help Window")
    help_text = "Error..."
    with open('help.txt', 'r') as f:
        help_text = f.read()
    label = ttk.Label(help_window, text=help_text)
    label.grid(padx=10, pady=10)

# create the menus
menubar = Menu(root)    # main menu
filemenu = Menu(root)   # file options menu

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Help", command=getHelp)

filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')

root.configure(menu=menubar)

# create the main frames used
resolution = ttk.Labelframe(root, text="Resolution:")
leftframe = StatementFrame(root)

# create the canvas to do the resolution on
canvas = ResolutionCanvas(resolution)
canvas.configure(bg='white')

# grid everything into the app
resolution.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky=(N,E,S,W))
leftframe.grid(row=0, column=0, sticky=(N,E,S,W))

canvas.grid(sticky=(N,E,S,W))

# setup a sizegrip item at the bottom right corner
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

# specify how columns and row expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=5)
root.grid_rowconfigure(0, weight=1)

resolution.grid_columnconfigure(0, weight=1)
resolution.grid_rowconfigure(0, weight=1)

leftframe.grid_columnconfigure(0, weight=1)
leftframe.grid_rowconfigure(0, weight=5)
leftframe.grid_rowconfigure(1, weight=1)

# start up the app
root.mainloop()
