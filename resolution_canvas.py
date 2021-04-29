from tkinter import *
from tkinter import ttk

class ResolutionCanvas(Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Double-1>", self.add_statement)

    def add_statement(self, event):
        # create the frame
        frame = ttk.Frame()
        frame.configure(relief="raised")
        frame.configure(padding=(5, 5))

        # make and grid the widgets in the frame
        text1 = ttk.Entry(frame, width=12)
        text1.grid(row=0)

        valid = ttk.Label(frame, text="invalid")
        valid.grid(row=1, sticky=(W))

        check = ttk.Button(frame, text="✓", width=3)
        check.grid(row=1, sticky=(E))

        # add the frame into the canvas at the click position
        id1 = self.create_window(event.x, event.y, window=frame, tags=("statement"))

        # add the various bindings needed
        self.tag_bind("statement", "<Button-1>", self.update_frame)

    def get_statement_frames(self):
        return self.find_withtag("statement")

    def update_frame(self, event):
        print(self.find_withtag("current"))
        print("hey")
        
