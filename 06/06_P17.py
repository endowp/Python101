rocks=[int(e) for e in input().split()]
player1=0
player2=0
c=0
while len(rocks)>0:
    if rocks[0]>rocks[-1]:
        score=rocks.pop(0)
    else:
        score=rocks.pop()
    if c%2==0:
        player1+=score
    else:
        player2+=score
    c+=1
if player1==player2:
    win=0
elif player1>player2:
    win=1
else:
    win=2
print(player1)
print(player2)
print(win)
        
