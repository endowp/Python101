n,t=[int(e) for e in input().split()]
c=1
r=n
countR=1
countC=1
if t==3:
    while c<=n:
        while r>0:
            print("(", c, ",", r, ")",sep="")
            r-=1
            c+=1
elif t==1:
    r=1
    c=1
    count=1
    while c<=n:
        r=count
        while r<=n:
            print("(", c, ",", r, ")",sep="")
            r+=1
        c+=1
        count+=1
elif t==2:
    r=1
    c=1
    count=1
    while r<=n:
        c=1
        while c<=count:
            print("(",r,",",c,")",sep="")
            c+=1
        r+=1
        count+=1
