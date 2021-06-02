floods=[int(e) for e in input().split(",")]
count=0
i=0
while i<len(floods):
    if floods[i]<0:
        count+=1
        while floods[i]<0:
            i+=1
    i+=1
print(count)
