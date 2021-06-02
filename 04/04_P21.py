num=int(input())
temp=""
prefix=""
suffix=""
n=0
while num>0:
    s=input()
    num-=1
    if n>=1:
        temp=s
        n=len(s)
    while n>0:
        if s[n]==temp[n]:
            prefix+=s[n]
        n+=1
print(prefix)
