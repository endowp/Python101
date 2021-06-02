row=int(input())
col=int(input())
data=[]
for i in range(row):
    data.append(input().split())
equal=[0]*row
j=0
while j<row:
    k=0
    while k<=col:
        if data[j] ==data[k]:
            equal[j]+=1
            equal[k]+=1
            break
        k+=1
    j+=1
e=0
while e<len(equal):
    if equal[e]%2==1:
        print(e+1)
        for n in data[e]:
            print(n,end=" ")
        print("")
    e+=1
