class Mammal:
    def walk(self):
        print('i can walk')
class Dog(Mammal):
    pass
class Cat(Mammal):
    def meow(self):
        print('my sound is meow')

cat1=Cat()
cat1.walk()
cat1.meow()