from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

from resolution_canvas import ResolutionCanvas
from statement_frame import StatementFrame

class ResolutionGUI():
    def __init__(self):
        # useful variables
        self.__version__ = 0.3

        # used to help transfer between subapps
        self.selected_clause_id = None

        # create the root window
        self.root = ThemedTk()
        self.root.title("Graphical Resolution " + str(self.__version__))
        self.root.option_add('*tearOff', FALSE)  # so the menu doesn't tear

        # create the menus
        self.create_menu()

        # create the main frames used
        self.resolution = ttk.Labelframe(self.root, text="Resolution:")
        self.leftframe = StatementFrame(self.root, self)

        # create the canvas to do the resolution on
        self.canvas = ResolutionCanvas(self.resolution, self)
        self.canvas.configure(bg='white')

        # setup a sizegrip item at the bottom right corner
        ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

        # grid the widgets and setup the expansions
        self.grid()
        self.set_row_col()

    # used to display the help menu
    def get_help(self, *args):
        help_window = Toplevel(self.root)
        help_window.title("Help Window")
        help_text = "Error..."
        with open('help.txt', 'r') as f:
            help_text = f.read()
        label = ttk.Label(help_window, text=help_text)
        label.grid(padx=10, pady=10)

    def update_clause_premise(self, index):
        # get the clause frame that is selected
        clause = self.canvas.frames[self.selected_clause_id]

        # if the selected is in a blank state, set the premise
        if clause.state == None:
            clause.state = "topclause"
            clause.premise_index = index
            clause.info.set("p: " + str(index))

        # if the selected is a top level clause, update it
        elif clause.state == "topclause":
            if clause.premise_index == index:
                clause.state = None
                clause.premise_index = None
                clause.info.set("invalid")
            else:
                clause.premise_index = index
                clause.info.set("p: " + str(index))

    def create_menu(self):
        # create the menus
        self.menubar = Menu(self.root)    # main menu
        self.filemenu = Menu(self.root)   # file options menu

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_command(label="Help", command=self.get_help)

        self.filemenu.add_command(label='Open')
        self.filemenu.add_command(label='Save')
        self.filemenu.add_command(label='Save As')

        self.root.configure(menu=self.menubar)

    # grid everything into the app
    def grid(self):
        self.resolution.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky=(N,E,S,W))
        self.leftframe.grid(row=0, column=0, sticky=(N,E,S,W))

        self.canvas.grid(sticky=(N,E,S,W))

    # specify how columns and row expand
    def set_row_col(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=5)
        self.root.grid_rowconfigure(0, weight=1)

        self.resolution.grid_columnconfigure(0, weight=1)
        self.resolution.grid_rowconfigure(0, weight=1)

        self.leftframe.grid_columnconfigure(0, weight=1)
        self.leftframe.grid_rowconfigure(0, weight=5)
        self.leftframe.grid_rowconfigure(1, weight=1)

    def start(self):
        self.root.mainloop()


# start up the app
if __name__ == "__main__":
    app = ResolutionGUI()
    app.start()
