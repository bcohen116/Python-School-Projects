from tkinter import *

class draw (Frame):
    myColor = ""
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Rectangle")
        self.master.geometry("400x400")

        self.myCanvas = Canvas(self)
        self.myCanvas.pack(expand = YES, fill = BOTH)

        self.myCanvas.bind("<Button-1>", self.paint)
        self.myCanvas.bind("<B1-Motion>", self.paint2)
        self.myCanvas.bind("<Button-3>", self.popUp)
    def popUp(self, event):
        toplevel = Toplevel()
        self.lbl = Label(toplevel, text = "Choose A Color:")
        self.lbl.pack(side = TOP)
        self.red = Button(toplevel, text = "red", command = self.redButton)
        self.red.pack()
        self.blue = Button(toplevel, text = "blue", command = self.blueButton)
        self.blue.pack()
        self.yellow = Button(toplevel, text = "yellow", command = self.yellowButton)
        self.yellow.pack()
        self.black = Button(toplevel, text = "black", command = self.blackButton)
        self.black.pack()
        
    def redButton(self):
        self.myColor = "red"   
    def blueButton(self):
        self.myColor = "blue"
    def blackButton(self):
        self.myColor = "black"   
    def yellowButton(self):
        self.myColor = "yellow" 
    def chooseColor(self, event):
        self.myColor = event.widget.get()
    def setRec(self):
        return self.myCanvas.create_rectangle()

    rectangle = setRec

    def paint(self, event):
        self.x1, self.y1 = (event.x - 4), (event.y - 4)

    def paint2(self, event):
        x2, y2 = (event.x + 4), (event.y + 4)
        self.myCanvas.delete(self.rectangle)
        self.rectangle = self.myCanvas.create_rectangle(self.x1, self.y1, x2, y2, fill=self.myColor, outline=self.myColor)
    
def main():
    draw().mainloop()
if __name__ == "__main__":
    main()
