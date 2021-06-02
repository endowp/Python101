n=int(input())
d={}
for i in range(n):
    line = input().split(", ")
    id, ad= line[0], line[1:]
    for subad in ad:
        if subad not in d:
            d[subad]={id}
        else:
            d[subad].add(id)
see=input().split(", ")
for s in see:
    if s in d:
        print(s, " -> ", ", ".join(sorted(d[s])))
    else:
        print(s, " -> Not found")
    


