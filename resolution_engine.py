from tkinter import *
from tkinter import ttk

class ResolutionEngine(ttk.Frame):
    def __init__(self, master, app, **kwargs):
        # initialize the frame
        super().__init__(master, **kwargs)

        # useful variables
        self.app = app      # the parent app

    def verify_all(self):
        print("Test successful")
        premise_listbox = self.app.leftframe.plist
        conclusion_listbox = self.app.leftframe.clist
        for i in range(premise_listbox.size()):
            print("Premise " + str(i) + ": " + str(premise_listbox.get(i)))
