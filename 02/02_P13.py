inh=int(input())
inm=int(input())
outh=int(input())
outm=int(input())
time=(outm+(outh*60))-(inm+(inh*60))
pay=0
if time>360:
    pay=200
else:
    if time>=180:
        pay+=10
        while (time-60)>180:
            pay+=20
            time-=60
    if time>15:
        pay+=10
        while (time-60)>0:
            pay+=10
            time-=60
print(pay)
    
