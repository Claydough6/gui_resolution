from tkinter import *
from tkinter import ttk

from edit_listbox import EditListbox

class StatementFrame(ttk.Frame):
    def __init__(self, master, app, **kwargs):
        # initialize the frame
        super().__init__(master, **kwargs)

        # useful variables
        self.app = app      # the parent app

        # initialize the sub frames
        self.statements = ttk.Labelframe(self, text="Statements:")
        self.tools = ttk.Frame(self)

        # create and grid the widgets
        self.create_widgets()
        self.grid_widgets()

    def create_widgets(self):
        # create the list of premises
        self.plist = EditListbox(self.statements, self.app, selectmode="browse")
        self.plist.colorize()

        # create the conclusion list
        self.clist = EditListbox(self.statements, self.app, selectmode="browse", height=1)
        self.clist.insert(0, "Conclusion")
        self.clist.color = "IndianRed1"
        self.clist.colorize()

        # create the scrollbar
        self.sbar = ttk.Scrollbar(self.statements, orient=VERTICAL, command=self.plist.yview)
        self.plist.configure(yscrollcommand=self.sbar.set)

        # create the buttons for the tools
        self.newPremise = ttk.Button(self.tools, text="New Premise", command=self.plist.add_premise)
        self.deletePremise = ttk.Button(self.tools, text="Delete Premise", command=self.plist.remove_premise)

    def grid_widgets(self):
        # grid the sets of widgets
        self.statements.grid(row=0, column=0, padx=5, pady=5, sticky=(N,E,S,W))
        self.tools.grid(row=1, column=0, padx=5)

        self.newPremise.grid(pady=2)
        self.deletePremise.grid(pady=2)

        self.plist.grid(row=0, column=0, sticky=(N,E,S,W))
        self.clist.grid(row=1, column=0, sticky=(E,W,S))
        self.sbar.grid(row=0, column=1, sticky=(N,S,E))

        # set the column and row configurations
        self.statements.grid_columnconfigure(0, weight=1)
        self.statements.grid_rowconfigure(0, weight=1)
        
