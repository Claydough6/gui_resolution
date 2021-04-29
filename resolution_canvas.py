from tkinter import *
from tkinter import ttk

class ResolutionCanvas(Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.active = None
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
        # note: need to add these

    def get_statement_frames(self):
        return self.find_withtag("statement")

    # used to drag the clause frames around the screen
    def move_frame(self, event):
        pass
        
