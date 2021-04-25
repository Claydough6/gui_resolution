from tkinter import *
from tkinter import ttk

# a fuction to modify the message variable
def addToMessage():
    temp = message.get()
    temp += '.'
    message.set(temp)

# create the main window
root = Tk()

# make a frame for the widget to live in
frame = ttk.Frame(root)
frame['padding'] = (5, 10)  # vertical, horizontal padding
frame['borderwidth'] = 2
frame['relief'] = 'ridge'  # just styling
frame.grid()

# create a label to display some text
message = StringVar()
message.set("hello")
label = ttk.Label(frame, textvariable=message)
label.grid()

# create a button for example (lives in the frame)
button = ttk.Button(frame, text="push me", command=addToMessage)
button.grid()

# update the theme of the test app
s = ttk.Style()
s.theme_use('clam')

# start up the frame
root.mainloop()
