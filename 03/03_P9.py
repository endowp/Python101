n=int(input())
count=n-1
numn=0
while count>=2:
    if n%count==0:
        numn+=1
        print(count, end=" ")
    count-=1
if numn==0:
    print("Prime Number")
    
