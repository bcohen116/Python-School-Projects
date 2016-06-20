'''
Created on Sep 29, 2014

@author: ben
'''
class Special(object):
    def __str__(self):
        return "%s" % Special.__name__
class Shape(object):
    def __str__(self):
        return "%s" % Shape.__name__
class Polygon(Shape):
    def __str__(self):
        return "%s\n     %s" % (Shape.__str__(self), Polygon.__name__)
class Parralelogram(Polygon):
    def __str__(self):
        return "%s\n          %s" % (Polygon.__str__(self), Parralelogram.__name__)

class Rectangle(Parralelogram):
    def __str__(self):
        return "%s\n               %s" % (Parralelogram.__str__(self), Rectangle.__name__)
class Square(Special, Rectangle):
    def __str__(self):
        return "%s\n%s\n                    %s" %  (Rectangle.__str__(self), Special.__str__(self), self.__class__.__name__)
s = Square()
print (s.__str__())