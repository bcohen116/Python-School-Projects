'''
Created on Sep 18, 2014

@author: ben
'''
disks = 3
start = 1
hold = 2
end = 3

def hanoi(disks,start,hold,end):
    if disks <= 0:
        x=1
        #STOP. IN THE NAME OF LOOOOOOOOOOOOOOOOOVE
    else:
        hanoi(disks-1,start,end,hold)
        print "%d --> %d" % (start, end)
        hanoi(disks-1,hold,start,end)



hanoi(disks, start, hold, end)

#def hanoi2(peg["Original", "helper", "target"]):
#    peg["Original"] = 1
#def hanoi(original, helper, target):
#    if target < pegs[0]:
#        if original > helper:
#            if original % 2 == 0:
#                original -= 1
#                target += 1
#                hanoi(original, helper, target)
#                return "1 --> 3 \n"
#            else:
#                original -= 1
#                helper += 1
#                hanoi(original, helper, target)
#                return "1 --> 2 \n"
#        elif helper > original:
#            if helper % 2 == 0:
#                helper -= 1
#                target += 1
#                hanoi(original, helper, target)
#                return "2 --> 3 \n"
#            else:
#                helper -= 1
#                original += 1
#                hanoi(original, helper, target)
#                return "2 --> 1 \n"
#        elif helper == original and helper == target:
#            original -= 1
#            target += 1
#            hanoi(original, helper, target)
#            return "2 --> 3 \n"
#        else:
#            if target % 2 == 0:
#                target -= 1
#                original += 1
#                hanoi(original, helper, target)
#                return "3 --> 1 \n"
#            else:
#                target -= 1
#                helper += 1
#                hanoi(original, helper, target)
#                return "3 --> 2 \n"
#    else:
#        return "Done"
#pegs = [3,0,0]
#print hanoi(pegs[0], pegs[1], pegs[2])
