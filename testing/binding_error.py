from tkinter import *
from tkinter import ttk

class ResolutionCanvas(Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.active = None
        self.bind("<Shift-1>", self.add_statement)
        # this shape is used to test the binding (this one works fine)
        id1 = self.create_rectangle((10, 10, 30, 30), fill="purple")
        self.tag_bind(id1, "<Button-1>", lambda x: print("box clicked"))

    def add_statement(self, event):
        # create the frame
        frame = ttk.Frame()
        frame.configure(relief="raised")
        frame.configure(padding=(50, 50))

        # make and grid the widgets in the frame
        text1 = ttk.Entry(frame, width=12)
        text1.grid(row=0)

        valid = ttk.Label(frame, text="invalid")
        valid.grid(row=1, sticky=(W))

        check = ttk.Button(frame, text="✓", width=3)
        check.grid(row=1, sticky=(E))

        # add the frame into the canvas at the click position
        id1 = self.create_window(event.x, event.y, window=frame, tags=("statement"))

        # add the various bindings needed (this is what is not working)
        self.tag_bind(id1, "<Button-1>", self.move_frame)

    def get_statement_frames(self):
        return self.find_withtag("statement")

    # used to drag the clause frames around the screen
    def move_frame(self, event):
        # note: this is just to see if the binding works for now
        print("frame clicked")

if __name__ == "__main__":
    root = Tk()
    canvas = ResolutionCanvas(root)
    canvas.grid()
    root.mainloop()
        
