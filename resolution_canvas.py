from tkinter import *
from tkinter import ttk

class ResolutionCanvas(Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.frames = dict()    # maps window id to frame
        
        self.bind("<Shift-1>", self.add_statement)
        self.bind("<Button-1>", self.select_frame)

    def add_statement(self, event):
        # create the frame
        frame = ttk.Frame()
        frame.configure(relief="flat")
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
        self.frames[id1] = frame
        
        # add the various bindings needed
        # note: need to add these

    def get_statement_frames(self):
        return self.find_withtag("statement")

    def select_frame(self, event):
        # if one selected, deselect it first
        self.deselect()     # removes selected tag

        # now bind some stuff
        self.bind('<Motion>', self.move_frame)
        self.bind('<ButtonRelease-1>', self.stop)

        # get selected frame (if applicable)
        for frame in self.get_statement_frames():
            c = self.bbox(frame)
            if c[0]-10 <= event.x <= c[2]+10 and c[1]-10 <= event.y <= c[3]+10:
                self.addtag_withtag('selected', frame)
                self.frames[frame].configure(relief="raised")
                break

    # used to drag the clause frames around the screen
    def move_frame(self, event):
        x, y = event.x, event.y
        self.coords('selected', x, y)

    def stop(self, event):
        self.unbind('<Motion>')

    def deselect(self):
        frames = self.find_withtag("selected")
        for frame in frames:
            self.frames[frame].configure(relief="flat")
        
        self.dtag("selected")
        
        
