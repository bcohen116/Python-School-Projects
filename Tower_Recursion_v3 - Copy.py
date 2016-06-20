from tkinter import *
import time
#import Image, ImageTk
"""
disks = 4
start = 1
hold = 2
end = 3
group = [disks, 0, 0]
def hanoi(disks, start, hold, end, number):
    if disks <= 0:
        x = "code"
    else:
        
        hanoi(disks - 1, start, end, hold, number)
        print ("",start,"-->",end)
        number[start-1] -= 1
        number[end-1] += 1
        print(number)
        hanoi(disks - 1, hold, start, end, number)
        
print (group)
hanoi(disks, start, hold, end, group)
"""
##################################

class draw (Frame):
    q = Button()
    myColor = ""
    def __init__(self):
        #four = ImageTK.PhotoImage(Image.open('4.jpg').convert2byte())
        #three = ImageTK.PhotoImage(Image.open('3.jpg').convert2byte())
        #two = ImageTK.PhotoImage(Image.open('2.jpg').convert2byte())
        #one = ImageTK.PhotoImage(Image.open('1.jpg').convert2byte())
        #zero = ImageTK.PhotoImage(Image.open('0.jpg').convert2byte())
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Hanoi")
        self.master.geometry("400x400")
        
            
        self.z = Button(self, text = "start", command = self.boo)
        self.z.pack()
    def boo(self):
        self.hanoi(3, 1, 2, 3, [3, 0, 0])
    def hanoi(self, disks, start, hold, end, number):
        self.createHanoi(number[0], number[1], number[2])
        
        if disks <= 0:
            x = "code"
            
        else:
            time.sleep(0.2)
            self.hanoi(disks - 1, start, end, hold, number)
            self.update()
            #print ("",start,"-->",end)
            number[start-1] -= 1
            number[end-1] += 1
            self.createHanoi(number[0], number[1], number[2])
            self.hanoi(disks - 1, hold, start, end, number)
        
        #hanoi(4, 1, 2, 3,[4, 0 ,0])

    q = [Button,Button,Button,Button,Button,Button,Button,Button,Button]
    shift = 0
    
    def clearShit(self):
        for x in range(9):
            #self.q[x].destroy(self)
            pass
    print("The numbers are the ring the pieces are on, the _ means next step.")       
    def createHanoi(self, one, two, three):
        #################self.pack(expand = YES, fill = BOTH)
        self.clearShit()
        self.d = Label(self, text = "").grid(row = 0, column = 0)
        for x in range(one):
            self.a = Label(self, text = "1").grid(row = 1, column = self.shift)
            self.q[x] = Button(self, text = "").grid(row = x+2, column = self.shift)
        for x in range(two):
            self.b = Label(self, text = "2").grid(row = 1, column = self.shift + 1)
            self.q[x] = Button(self, text = "").grid(row = x+2, column = self.shift + 1)
        for x in range(three):
            self.c = Label(self, text = "3").grid(row = 1, column = self.shift + 2)
            self.q[x] = Button(self, text = "").grid(row = x+2, column = self.shift + 2)
        #for x in range(3):
        self.z = Label(self, text = "_").grid(row = 2, column = self.shift + 3)
        
        self.shift += 5
        
def main():
    draw().mainloop()
if __name__ == "__main__":
    main()
