import random

items=['Rock','Paper','Scissor']

for i in items:
    res=random.choice(items)
for j in items:
    res2=random.choice(items)

print("P1:"+res,"P2:"+res2)

if(res==res2):
    print("Tied")
elif(res=='Rock' and res2=='Scissor'):
    print('Player 1 win')
elif(res=='Scissor' and res2=='Paper'):
    print('Player 1 win')
elif(res=='Paper' and res2=='Rock'):
    print('Player 1 wins')
else:
    print('Player 2 wins')