'''
Created on Oct 31, 2014

@author: Ben
'''
from tkinter import *    # Python 3

class DrawTest (Frame):
    """Demonstrate GUI functionality"""

    myColor = ""
    def __init__(self):
        """Create some GUI components and bind some events"""

        super().__init__()

        # Create a drawing window

        #self.master = Toplevel()
        #self.master.title("A drawing window")
        #self.master.geometry("600x300")

        self.myPanel = Toplevel()
        self.myPanel.title("A drawing window")
        self.myPanel.geometry("600x300")


        # Add the Canvas component to the drawing window

        self.myCanvas = Canvas(self.myPanel)
        #self.myCanvas = Canvas(self.master)
        self.myCanvas.pack(expand=YES, fill=BOTH)

        # Bind mouse dragging event to Canvas

        self.myCanvas.bind("<Button-1>", self.paint)
        self.myCanvas.bind("<ButtonRelease-1>", self.paint3)
        self.myCanvas.bind("<ButtonRelease-3>", self.colorPrompter())

    def chooseColor(self, event):
        self.myColor = event.widget.get()

    x1 = 0
    y1 = 0

    def setRec(self):
        return self.myCanvas.create_rectangle()

    rectangle = setRec

    def paint(self, event):
        self.x1, self.y1 = (event.x - 4), (event.y - 4)

    def paint3(self, event):
        x2, y2 = (event.x + 4), (event.y + 4)
        self.myCanvas.delete(self.rectangle)
        self.rectangle = self.myCanvas.create_rectangle(self.x1, self.y1, x2, y2, fill="black")

    def colorPrompter(self):
        #self.pack(expand=YES, fill=BOTH)
        #self.title("A simple GUI program")
        #self.geometry("250x50")

        self.pack(expand=YES, fill=BOTH)
        self.master.title("A simple GUI program")
        self.master.geometry("250x50")

        # Create an entry for choosing a color

        self.colorPrompt = Label(self, text="Please enter a color:")
        self.colorPrompt.pack(side=LEFT)

        self.colorChooser = Entry(self, name="colorChooser")
        self.colorChooser.bind("<Return>", self.chooseColor)
        self.colorChooser.pack(side=RIGHT)
        self.rectangle.fill(self.myColor)
        self.rectangle.outline(self.myColor)



def main():
    DrawTest().mainloop()

if __name__ == "__main__":
    main()
