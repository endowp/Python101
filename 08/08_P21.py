num=set(int(e) for e in input().split())
num2=int(input())
c=0
for i in num:
    if num2-i in num:
        c+=1
print(int(c/2))
