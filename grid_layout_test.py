from tkinter import *
from tkinter import ttk

# create the root window
root = Tk()

# create the main frame of the program and the sub frame
content = ttk.Frame(root)
subframe = ttk.Frame(content, borderwidth=5, relief='sunken')
topframe = ttk.Frame(content, borderwidth=5, relief='raised', width=200, height=100)

# make the checks to go in the subframe
c1 = ttk.Checkbutton(subframe, text="One")
c2 = ttk.Checkbutton(subframe, text="Two")
c3 = ttk.Checkbutton(subframe, text="Three")
ok = ttk.Button(subframe, text="Click Me!")

# make the text box to enter stuff into
label = ttk.Label(content, text="Enter some text:")
box = ttk.Entry(content)

# lay everything out in the app
content.grid(column=0, row=0)
#topframe.grid(column=0, row=0, columnspan=5, rowspan=2)
subframe.grid(column=0, row=2, columnspan=5)

c1.grid(column=0, row=2)
c2.grid(column=1, row=2)
c3.grid(column=2, row=2)
ok.grid(column=3, row=2, columnspan=2)

label.grid(column=3, row=0, columnspan=2)
box.grid(column=3, row=1, columnspan=2)

# run the app
root.mainloop()
