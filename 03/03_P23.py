n=int(input())
d=int((n/2)-1)
s=int((n-(n-1)))
count=0
for i in range(int(((n*2)+1)/4)):
    print("."*d,end="")
    print("#"*s,end="")
    if n%2!=0:
        print("#",end="")
    print("#"*s,end="")
    print("."*d,end="")
    print("."*(d+1),end="")
    print("#"*s,end="")
    if n%2!=0:
        print("#",end="")
    print("#"*s,end="")
    print("."*(d),end="")
    print("")
    d-=1
    s+=1
for k in range((n//2)-2):
    print("#"*((n*2)+1))
d=0
s=n
for j in range(n+1):
    print("."*(d),end="")
    print("#"*s,end="")
    print("#"*1,end="")
    print("#"*(s),end="")
    print("."*(d),end="")
    print("")
    d+=1
    s-=1
