n=int(input())
count=n-1
numn=0
primefac=[]
while count>=2:
    if n%count==0:
        primefac.append(count)
        numn+=1
    count-=1
    for i in primefac:
        count2=i-1
        numn2=0
        primefac2=[]
        while count2>=2:
            if i%count2==0:
                #if numn2==0:
                primefac2.append(count2)
                #numn2+=1
            count2-=1
for j in primefac2:
    print(j,end=" ")
