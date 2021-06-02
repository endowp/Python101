num=list((input()))
count=[0]*10
for n in num:
    i=0
    while i<=10:
        if int(n)==i:
            count[i]+=1
        i+=1
for c in count:
    print(c)
