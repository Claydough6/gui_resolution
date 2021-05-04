from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog

from resolution_canvas import ResolutionCanvas
from statement_frame import StatementFrame
from resolution_engine import ResolutionEngine
from info_window import InfoWindow

class ResolutionGUI():
    def __init__(self):
        # useful variables
        self.__version__ = 0.3
        self.filename = None

        # used to help transfer between subapps
        self.selected_clause_id = None

        # create the root window
        self.root = ThemedTk()
        self.root.title("Graphical Resolution " + str(self.__version__))
        self.root.option_add('*tearOff', FALSE)  # so the menu doesn't tear

        # create the rules for the application
        self.rules = ResolutionEngine(self.root, self)

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
        help_window = InfoWindow(self.root, "Help Window", "help.txt", file=True)

    # used to display an error to the user
    def show_error(self, error_text):
        error_window = InfoWindow(self.root, "Error Window!", error_text)

    def update_clause_premise(self, index, conclusion=False):
        # get the clause frame that is selected
        clause = self.canvas.frames[self.selected_clause_id]

        # if the selected is in a blank state, set the premise
        if clause.state == None:
            clause.state = "topclause"
            # deal with conclusion vs premise list
            if not conclusion:
                clause.premise_index = index
                clause.info.set("p: " + str(index))
            else:
                clause.premise_index = -1
                clause.info.set("c")

        # if the selected is a top level clause, update it
        elif clause.state == "topclause":
            if conclusion:
                index = -1
            if clause.premise_index == index:
                clause.state = None
                clause.premise_index = None
                clause.info.set("invalid")
            else:
                # deal with conclusion vs premise list
                if not conclusion:
                    clause.premise_index = index
                    clause.info.set("p: " + str(index))
                else:
                    clause.premise_index = -1
                    clause.info.set("p: c")

    def create_menu(self):
        # create the menus
        self.menubar = Menu(self.root)    # main menu
        self.filemenu = Menu(self.root)   # file options menu

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_command(label="Help", command=self.get_help)

        self.filemenu.add_command(label='Open', command=self.open)
        self.filemenu.add_command(label='Save', command=self.save)
        self.filemenu.add_command(label='Save As', command=self.saveas)

        self.root.configure(menu=self.menubar)

    def save(self, *args):
        #InfoWindow(self.root, "Save Window!", self.canvas.get_save_string())
        if not self.filename:
            self.saveas()
        else:
            savestr = ""
            savestr += self.leftframe.get_save_string()
            savestr += self.canvas.get_save_string()
            with open(self.filename, 'w') as f:
                f.write(savestr)

    def saveas(self, *args):
        self.filename = filedialog.asksaveasfilename()
        self.save()

    def open(self, *args):
        # see if we should save first?

        # get the file
        self.filename = filedialog.askopenfilename()

        savestr = ""
        with open(self.filename, 'r') as f:
            savestr = f.read()

        # populate the app with the file info
        self.canvas.open(savestr)
        self.leftframe.open(savestr)

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
