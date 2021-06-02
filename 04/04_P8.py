s=str(input())
n1,n2=[int(e) for e in input().split()]
j=0
for i in range(len(s)):
    if j<n1-1:
        print(s[j],end="")
        j+=1
    elif j>=n1-1:
        j=n2
        if j>=n1:
            print(s[j],end="")
            j-=1
        elif j<=k:
            print(s[j],end="")
            j+=1
        k=n2-1
