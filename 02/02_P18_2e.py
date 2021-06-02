a1,b1,c1=input().split()
a2,b2,c2=input().split()
a1=int(a1)
a2=int(a2)
b1=int(b1)
b2=int(b2)
c1=int(c1)
c2=int(c2)
n=0
x=-101
while x<100:
    x+=0.25
    y=-101
    while y<100:
        y+=0.25
        if (a1*x)+(b1*y)+c1==0 and (a2*x)+(b2*y)+c2==0:
            n+=1
if n==0:
    print("no solution")
elif n==1:
    print("one solution")
else:
    print("many solutions")
