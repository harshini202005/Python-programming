'''class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        print('draw')
p1=Point(10,20)
p1.x=11
print(p1.x)'''

class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f' hi {self.name}')
per=Person('john')
per.talk()
per1=Person('Bob')
per1.talk()