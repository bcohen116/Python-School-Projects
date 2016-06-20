'''
Created on Sep 18, 2014

@author: ben
'''
disks = 4
start = 1
hold = 2
end = 3

def hanoi(disks, start, hold, end):
    if disks <= 0:
        x = 1
        #STOP. IN THE NAME OF LOOOOOOOOOOOOOOOOOVE
    else:
        hanoi(disks - 1, start, end, hold)
        print ("%d --> %d") % (start, end)
        hanoi(disks - 1, hold, start, end)



hanoi(disks, start, hold, end)

