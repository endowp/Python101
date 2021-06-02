m,y =(input().split())
newy=int(y)-543
m=int(m)
if m==2:
    if newy%400==0 or (newy%4==0 and newy%100!=0):
        d=29
    else:
        d=28
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    d=31
else:
    d=30
print(d)
    
