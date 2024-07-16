class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(f"I'm {self.firstname} {self.lastname}")

class Student(Person):
    pass
s1=Student('Deep','H')
s1.printname()
