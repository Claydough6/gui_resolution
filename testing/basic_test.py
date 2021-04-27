from tkinter import *
from tkinter import ttk

# a fuction to modify the message variable
def addToMessage():
    temp = message.get()
    temp += '.'
    message.set(temp)

# a function to be used with the entry box
def modText(window):
    text = entered.get()
    for i in range(len(text)):
        if i % 2 == 0:
            text = text[:i] + text[i].upper() + text[i+1:]
        else:
            text = text[:i] + text[i].lower() + text[i+1:]
    display.set(text)

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

# create a check box thing and display some text
checkValue = StringVar()
check = ttk.Checkbutton(frame, text="are you happy?", variable=checkValue, onvalue=":)", offvalue=":(")
check.grid()
face = ttk.Label(frame, textvariable=checkValue)
face.grid()

# create a radiobutton and display some text
question = ttk.Label(frame, text="Who are you?")
question.grid()
name = StringVar()
clay = ttk.Radiobutton(frame, text="Clay", variable=name, value="Hello Clay!")
kevin = ttk.Radiobutton(frame, text="Kevin", variable=name, value="Hello Kevin!")
clay.grid()
kevin.grid()
namelabel = ttk.Label(frame, textvariable=name)
namelabel.grid()

# create a text entry box and print out the value modified
# note for some reason this takes a while to update...
instruction = ttk.Label(frame, text="Enter some text then press enter.")
entered = StringVar()
display = StringVar()
entry = ttk.Entry(frame, textvariable=entered)
entry.bind("<Enter>", modText)
output = ttk.Label(frame, textvariable=display)
instruction.grid()
entry.grid()
output.grid()

# update the theme of the test app
s = ttk.Style()
s.theme_use('clam')

# start up the frame
root.mainloop()
