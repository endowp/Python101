n=int(input())
li=[]
new=[1]
i=1
j=0
while j < n:
    li.append(int(input()))
    j+=1
while len(new)<len(li):
    if li[i-1] != 1:
        new.append(li[i-1])
        i=li[i-1]
    else:
        i+=1
for num in new:
    print(num, end=" ")
