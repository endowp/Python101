import math
c=input().strip()
if c=="S":
    m=int(input().strip())
    q=1
    r=0
    t=1
    k=1
    n=3
    x=3
    i=0
    p=""
    while i<m:
        if 4*q+r-t<n*t:
            p=p+str(n)
            i=i+1
            a=10*(r-(n*t))
            n=10*(3*q+r)//t-(10*n)
            q=10*q
            r=a
        else:
            a=((2*q)+r)*x
            b=((7*q*k)+2+(x*r))//(x*t)
            q=k*q
            t=x*t
            x=x+2
            k=k+1
            n=b
            r=a
    p=p[0]+"."+p[1:]
elif c=="R":
    n=int(input().strip())
    k=0
    p=0
    while k<=n:
        p+=((-3)**(-k))/((2*k)+1)
        k+=1
    p=p*(12**(0.5))
    p=round(p,12)
elif c=="P":
    p=math.sqrt(7+(math.sqrt(6+(math.sqrt(5)))))
    p=round(p,6)
else:
    print("Invalid")
if c=="S" or c=="R" or c=="P":
    print("pi =", p)
