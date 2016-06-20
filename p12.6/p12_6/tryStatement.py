'''
Created on Oct 16, 2014

@author: Ben
'''
class trytester():
    def __init__(self, aNumber, aString):
        try:
            aNumber = int(aNumber)
            aString = "%s" % aString
        except ValueError:
            print ("You entered an incorrect format.")
        except:
            print ("An error has occurred.")
        else:
            print ("Test Success!")
t = trytester(input("Enter a number: "), input("Enter a string: "))