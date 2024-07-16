'''try:
    age=int(input('enter the age:'))
    print(age)
except ValueError:
    print('invalid input')'''
try:
    num=int(input('enter the number:'))
    print(num/0)
except ZeroDivisionError:
    print('cant divide by zero')
