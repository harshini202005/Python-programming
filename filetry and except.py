import os
filename=input("enter file:")
try:
    f=open(filename,"r")
    for line in f:
        print(line,end="")
    f.close()
except FileNotFoundError:
    print('not found')
except FileExistsError:
    print('no permission')
else:
    print('success')