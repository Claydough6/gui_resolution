from tkinter import *
from tkinter import ttk

# used to hide / show the feather
def updateFeather():
    if pic.winfo_viewable():
        pic.grid_remove()
        namelbl.grid_remove()
    else:
        pic.grid()
        namelbl.grid()

# create the root window
root = Tk()
root.title("Feather Window")
root.option_add('*tearOff', FALSE)  # so the menu doesn't look weird

# create the main frame of the program and the sub frame
content = ttk.Frame(root)
subframe = ttk.Frame(content, borderwidth=5, relief='sunken')

# create a menu
menubar = Menu(root)
sub1 = Menu(root)

menubar.add_cascade(label="test1", menu=sub1)

sub1.add_command(label='a')
sub1.add_command(label='b')
sub1.add_command(label='c')

root.configure(menu=menubar)

# make the checks to go in the subframe
c1 = ttk.Checkbutton(subframe, text="One")
c2 = ttk.Checkbutton(subframe, text="Two")
c3 = ttk.Checkbutton(subframe, text="Three")
ok = ttk.Button(subframe, text="Click Me!", command=updateFeather)

# put the image in another box
imageframe = ttk.Frame(content, borderwidth=5, relief='raised')
feather = PhotoImage(file="feather.png")
pic = ttk.Label(imageframe)
pic['image'] = feather

# make the text box to enter stuff into and name feather
name = StringVar()
label = ttk.Label(content, text="Name the feather:")
box = ttk.Entry(content, textvariable=name)
namelbl = ttk.Label(imageframe, textvariable=name)

# lay everything out in the app
content.grid(column=0, row=0)
subframe.grid(column=0, row=2, columnspan=5 ,pady=5)
imageframe.grid(column=0, row=0, columnspan=3, rowspan=2)

c1.grid(column=0, row=2, padx=5)
c2.grid(column=1, row=2, padx=5)
c3.grid(column=2, row=2, padx=5)
ok.grid(column=3, row=2, columnspan=2, padx=5)

label.grid(column=3, row=0, columnspan=2, padx=15)  # pad edges nicely
box.grid(column=3, row=1, columnspan=2, padx=15)
pic.grid()
namelbl.grid(sticky=E)

# give weights to the row and column expansions
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)

subframe.columnconfigure(0, weight=1)
subframe.columnconfigure(1, weight=1)
subframe.columnconfigure(2, weight=1)
subframe.columnconfigure(3, weight=1)
subframe.columnconfigure(4, weight=1)

# run the app
root.mainloop()
