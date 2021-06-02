n=int(input())
union=intersec=0
if n>1:
    s1=set(int(e) for e in input().split())
    for i in range(n-1):
        s2=set(int(e) for e in input().split())
        if union==0:
            union=s1 | s2
        if intersec==0:
            intersec=s1 & s2
        elif union!=0:
            union=union | s2
        elif intersec!=0:
            intersec=intersec & s2
        s1=s2
    print(len(union))
    print(len(intersec))
elif n==1:
    s1=set(int(e) for e in input().split())
    print(len(s1))
    print(len(s1))
else:
    print(0)
    print(0)
    
