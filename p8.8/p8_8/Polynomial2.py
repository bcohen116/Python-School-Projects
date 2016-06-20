'''
Created on Oct 23, 2014

@author: Ben
'''
class Polynomial():
    def __init__(self, numbers):
        self.nums = numbers
    def __getlen__(self):
        count = 0
        for x in self.nums.keys():
            if x > count:
                count= x
        return count
    def __getitem__(self, key):
        """Overloaded key-value access."""
        return self.nums[key]
    def __sub__(self, other):
        a = dict
        for x in self.nums.keys():
            for y in other.nums.keys():
                if (x==y):
                    a = {x, self.nums[x] - other.nums[y]}
                    return(a)
                else:
                    return ("%d - %d" % (self, other))
    def __add__(self, other):
        a = dict
        for x in self.nums.keys():
            for y in other.nums.keys():
                if (x==y):
                    a = {x, self.nums[x] + other.nums[y]}
                    return(a)
                else:
                    return ("%d + %d" % (self, other))
    def __str__(self):
        test = ""
        for x in self.nums.keys():
            test += "+ %dx^%d " %(self.nums[x], x)
        return test
dic = {1:2, 5:3, 3:4}
x = Polynomial(dic)
print(x.__str__())
print("Highest: %d" % x.__getlen__())
