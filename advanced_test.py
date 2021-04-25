from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

# create main root window
root = ThemedTk(theme="breeze")

# string vars used
nlist = ["Line {} of 100".format(i) for i in range(1, 101)]
names = StringVar(value=nlist)
display = StringVar()

# used to update the selection text
def updateSelection(*args):
    selection = lbox.curselection()[0]
    display.set("Selection: " + nlist[selection][:7].strip())

# create the listbox of lines
lbox = Listbox(root, listvariable=names, selectmode="browse", height=10)
lbox.bind("<<ListboxSelect>>", updateSelection)

# colorize alternating lines of the listbox
for i in range(0,len(nlist),2):
    lbox.itemconfigure(i, background='#EAEAEA')

# create the scrollbar
sbar = ttk.Scrollbar(root, orient=VERTICAL, command=lbox.yview)
lbox.configure(yscrollcommand=sbar.set)

# create the selection label
label = ttk.Label(root, textvariable=display)

# palce the widgets
lbox.grid(column=0, row=0, sticky=(N,E,S,W))
sbar.grid(column=1, row=0, sticky=(N,S))
label.grid(column=0, row=1)

# configure grid
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# setup a sizegrip item at the bottom right corner
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

# loop
root.mainloop()
