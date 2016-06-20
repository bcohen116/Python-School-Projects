'''
Created on Oct 16, 2014

@author: Ben
'''
from p9_8.fig09_09 import *
class Date(Employee):
    day = 0
    month = ""
    year = 0
    def __init__(self, aDay, aMonth, aYear, departmentCode):
        salary = int(input("Enter the worker's salary: "))
        super(self, "firstname","lastname", salary, birthDate, departmentCode)
        day = aDay
        month = aMonth
        year = aYear
class birthDate(Date):
    day = 0
    month = ""
    year = 0
    def __init__(self, aDay, aMonth, aYear):
        super(int(input("Enter the current date: ")), input("Enter the current month: "),
              int(input("Enter the current year: ")), int(input("Enter the worker's department code: ")))
        day = aDay
        month = aMonth
        year = aYear
        if (self.month == super().month):
            self.earnings().salary += 100
newBirthdate = birthDate(int(input("Enter your birthdate: ")), input("Enter your birth month: "), int(input("Enter your birth-year: ")))
print (newBirthdate.earnings())