a1,b1,c1=input().split()
a2,b2,c2=input().split()
a1=int(a1)
a2=int(a2)
b1=int(b1)
b2=int(b2)
c1=int(c1)
c2=int(c2)
if a1==0 and a2==0:
    a1==1
    a2==1
if b1==0 and b2==0:
    b1=1
    b2=1
if a1==0 and b2==0:
    a1=1
    b2=1
if a2==0 and b1==0:
    a2=1
    b1=1
if c1==0 and c2==0:
    c1=1
    c2=1
if ((a1%a2==0)or(a2%a1==0))and((b1%b2==0)or(b2%b1==0))and((c1%c2==0)or(c2%c1==0)):
    print("many solutions")                                                    
elif (((-1*a1)/b1)==((-1*a2)/b2))and c1==c2:
    print("many solutions")
elif ((-1*a1)/b1)==((-1*a2)/b2)and c1!=c2:
    print("no solution")
else:
    print("one solution")
