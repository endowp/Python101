s=str(input())
n1,n2=[int(e) for e in input().split()]
count=0
count2=1
for i in range(n1):
    print(s[i],end="")
for i in range(n2-n1+1):
    print(s[n2-count],end="")
    count+=1
for i in range(len(s)-n2-1):
    print(s[n2+count2],end="")
    count2+=1
