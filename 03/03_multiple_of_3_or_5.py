i=int(input())
c=3 #count
t=0 #total
while c<i:
    if c%3==0 or c%5==0:
        t+=c
    c+=1
print(t)
