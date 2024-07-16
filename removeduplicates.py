a=[2,5,6,2,3,5]
uniques=[]
for i in a:
    if i not in uniques:
        uniques.append(i)
print(uniques)