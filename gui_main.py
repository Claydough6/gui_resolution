from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

# create the root window
root = ThemedTk(theme="breeze")
root.title("Graphical Resolution")
root.option_add('*tearOff', FALSE)  # so the menu doesn't tear

# used to display the help menu
def getHelp(*args):
    help_window = Toplevel(root)
    help_window.title("Help Window")
    help_text = "This is where the directions go..."
    label = ttk.Label(help_window, text=help_text)
    label.grid(padx=10, pady=10)

# create the menus
menubar = Menu(root)    # main menu
filemenu = Menu(root)   # file options menu'

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Help", command=getHelp)

filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')

root.configure(menu=menubar)

# create the main frames used
resolution = ttk.Labelframe(root, text="Resolution:", relief="raised")
resolution['width'] = 500
resolution['height'] = 400

statements = ttk.Labelframe(root, text="Statements")
statements['width'] = 100
statements['height'] = 250

tools = ttk.Frame(root)
tools['width'] = 100
tools['height'] = 150

# grid everything into the app
resolution.grid(row=0, column=1, rowspan=3, padx=5, pady=5)
statements.grid(row=1, column=0, padx=5)
tools.grid(row=2, column=0, padx=5)

# start up the app
root.mainloop()
