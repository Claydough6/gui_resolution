from tkinter import *
from tkinter import ttk

# create the main window
root = Tk()

# make a frame for the widget to live in
frame = ttk.Frame(root)
frame['padding'] = (5, 10)  # vertical, horizontal padding
frame['borderwidth'] = 2
frame['relief'] = 'ridge'  # just styling
frame.grid()

# create a button for example (lives in the frame)
button = ttk.Button(frame, text="push me")
button.grid()

# update the theme of the test app
s = ttk.Style()
s.theme_use('xpnative')

# start up the frame
root.mainloop()
