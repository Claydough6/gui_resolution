import tkinter as tk


class App(tk.Tk):
    radius = 20

    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=500, height=500, bg='beige')
        self.canvas.pack()

        self.canvas.bind('<1>', self.select_circle)
        self.canvas.bind('<Shift-1>', self.make_circle)

        self.selected = None

    def make_circle(self, event):
        x, y, r = event.x, event.y, self.radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, outline='black', fill='white')

    def select_circle(self, event):
        self.canvas.bind('<Motion>', self.move_circle)
        self.canvas.bind('<ButtonRelease-1>', self.deselect)

        self.canvas.addtag_withtag('selected', tk.CURRENT)

    def move_circle(self, event):
        x, y, r = event.x, event.y, self.radius
        self.canvas.coords('selected', x-r, y-r, x+r, y+r)

    def deselect(self, event):
        self.canvas.dtag('selected')    # removes the 'selected' tag
        self.canvas.unbind('<Motion>')
        self.canvas.bind('<Shift-1>', self.make_circle)

if __name__ == '__main__':

    App().mainloop()
