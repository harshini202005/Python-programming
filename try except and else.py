try:
    age=int(input('enter the age'))
    income=20000/age
except ZeroDivisionError:
    print('age cant be zero')
except ValueError:
    print('age is invalid')
else:
    print('program over')
finally:
    print('hi')