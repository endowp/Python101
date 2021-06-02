file=open("books.txt")
d={}
sortinvolve=()
find=input().strip().split(", ")
for line in file:
    line=line.strip().split(", ")
    for involve in  line[1:]:
        if involve not in d:
            d[involve] = {line[0]}
        else:
            d[involve].add(line[0])
        if line[0] not in sortinvolve:
            sortinvolve+=(line[0], )
dcount=set()
for f in find:
    if f in d:
        for v in d.values():
            for subv in v:
                 if subv in d[f]:
                     if subv not in dcount:
                        dcount.add(subv)
                        break
    else:
        print("Not Found")
        exit()
intersec=set(sortinvolve)
for f in find:
    intersec =intersec & d[f]
if len(intersec)>0:
    for s in sortinvolve:
        for inter in intersec:
            if inter==s:
                print(inter)
else:
    print("Not Found")
