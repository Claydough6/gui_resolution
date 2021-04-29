from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

from edit_listbox import EditListbox
from resolution_canvas import ResolutionCanvas

__version__ = 0.1

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
leftframe = ttk.Frame(root)

statements = ttk.Labelframe(leftframe, text="Statements:")
tools = ttk.Frame(leftframe)

# create the list of premises
plist = EditListbox(statements, selectmode="browse")
plist.colorize()

# create the conclusion list
clist = EditListbox(statements, selectmode="browse", height=1)
clist.insert(0, "Conclusion")
clist.color = "IndianRed1"
clist.colorize()

# create the buttons for the tools
newPremise = ttk.Button(tools, text="New Premise", command=plist.add_premise)
deletePremise = ttk.Button(tools, text="Delete Premise", command=plist.remove_premise)

# create the canvas to do the resolution on
canvas = ResolutionCanvas(resolution)
canvas.configure(bg='white')

# create the scrollbar
sbar = ttk.Scrollbar(statements, orient=VERTICAL, command=plist.yview)
plist.configure(yscrollcommand=sbar.set)

# grid everything into the app
resolution.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky=(N,E,S,W))
leftframe.grid(row=0, column=0, sticky=(N,E,S,W))

statements.grid(row=0, column=0, padx=5, pady=5, sticky=(N,E,S,W))
tools.grid(row=1, column=0, padx=5)

newPremise.grid(pady=2)
deletePremise.grid(pady=2)

canvas.grid(sticky=(N,E,S,W))

plist.grid(row=0, column=0, sticky=(N,E,S,W))
clist.grid(row=1, column=0, sticky=(E,W,S))
sbar.grid(row=0, column=1, sticky=(N,S,E))

# setup a sizegrip item at the bottom right corner
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

# specify how columns and row expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=5)
root.grid_rowconfigure(0, weight=1)

resolution.grid_columnconfigure(0, weight=1)
resolution.grid_rowconfigure(0, weight=1)

leftframe.grid_columnconfigure(0, weight=1)
leftframe.grid_rowconfigure(0, weight=2)
leftframe.grid_rowconfigure(1, weight=1)

statements.grid_columnconfigure(0, weight=1)
statements.grid_rowconfigure(0, weight=1)

# start up the app
root.mainloop()
