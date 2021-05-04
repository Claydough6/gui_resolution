from tkinter import *
from tkinter import ttk

class ClauseFrame(ttk.Frame):
    def __init__(self, app, canvas, master=None, **kwargs):
        # useful variables
        self.text = StringVar()
        self.info = StringVar()
        self.info.set("invalid")
        
        self.id = None
        self.app = app
        self.canvas = canvas
        
        self.parents = list()
        self.child = None
        self.premise_index = None

        self.state = None
        
        # initialize the frame
        super().__init__(master, **kwargs)

        # make and grid the text entry in the frame
        self.text1 = ttk.Entry(self, width=12, textvariable=self.text)
        self.text1.grid(row=0)

        # make and grid the valid text in the frame
        self.valid = ttk.Label(self, textvariable=self.info)
        self.valid.grid(row=1, sticky=(W))

        # make and grid the check button in the frame
        self.check = ttk.Button(self, text="✓", width=3)
        self.check.grid(row=1, sticky=(E))

        # bindings
        self.bind("<Button-1>", self.clicked)
        self.valid.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        self.canvas.frame_click(self.id)

