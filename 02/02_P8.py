d=int(input())
m=int(input())
y=int(input())
newy=y-543
tot=d
while m>1:
    if m==2:
        if newy%400==0 or (newy%4==0 and newy%100!=0):
            tot+=29
            m-=1
            print(2,29)
        else:
            tot+=28
            m-=1
            print(2,28)
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        tot+=31
        print(m,31)
        m-=1
    else:
        tot+=30
        print(m,30)
        m-=1
print(1,d)
print(tot)
