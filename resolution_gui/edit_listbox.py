from tkinter import *

# a listbox class to be used for premises and conclusions
class EditListbox(Listbox):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        # variables
        self.edit_index = None
        self.color = None
        self.conclusion = False
        self.list = list()  # keeps the items
        self.app = app      # the parent app

        # bindings
        self.bind("<Double-1>", self.edit)
        self.bind("<Button-1>", self.click)

    def get_index(self, event):
        return self.index("@{},{}".format(event.x, event.y))

    def click(self, event):
        index = self.get_index(event)
        if self.app.selected_clause_id != None:
            self.app.update_clause_premise(index, self.conclusion)
        

    # used to add an entry box and edit the list
    def edit(self, event):
        # get and store the index
        index = self.get_index(event)
        self.edit_index = index

        # get the text and coordinates
        text = self.get(index)
        coords = self.bbox(index)
        y_coord = None
        if coords:
            y_coord = coords[1]
        else:
            return

        # create the entry box
        textbox = Entry(self, borderwidth=0, highlightthickness=1)
        textbox.bind("<Return>", self.add_edit)
        textbox.bind("<Escape>", self.reject_edit)

        # actually populate the entry box with text
        textbox.insert(0, text)
        textbox.selection_from(0)
        textbox.selection_to("end")

        # place and focus the box
        textbox.place(relx=0, y=y_coord, relwidth=1, width=-1)
        textbox.focus_set()
        textbox.grab_set()

    # used to update the list with the new entry
    def add_edit(self, event):
        new_text = event.widget.get()
        self.delete(self.edit_index)
        self.insert(self.edit_index, new_text)
        self.colorize()
        event.widget.destroy()

    # used to trash the changes
    def reject_edit(self, event):
        event.widget.destroy()

    # used to update the colors to maintain white-grey scheme
    def colorize(self):
        for i in range(0, self.size()):
            if i % 2 == 0:
                if self.color:
                    self.itemconfigure(i, background=self.color)
                else:
                    self.itemconfigure(i, background='#EAEAEA')
            else:
                self.itemconfigure(i, background='white')   

    # used to add a new premise to the list
    def add_premise(self):
        self.insert("end", "New Premise")
        self.colorize()

    # used to get rid of a premise clicked on
    def remove_premise(self):
        select = self.curselection()
        if not select:
            return
        index = select[0]
        self.delete(index)
        self.colorize()

    def get_save_string(self):
        string = "<premise>\n"
        for i in range(self.size()):
            text = self.get(i)
            string += text + "\n"
        string += "<\premise>\n"
        return string
            
            
        
