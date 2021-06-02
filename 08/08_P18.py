d={}
bts=input().strip().split()
go=set()
while len(bts)>1:
    station1, station2 = bts
    if station1 not in d:
        d[station1] = {station2}
    elif  station1 in d:
        d[station1].add(station2)
    if station2 not in d:
        d[station2] = {station1}
    elif station2 in d:
        d[station2].add(station1)
    bts=input().strip().split()
if "".join(bts) not in d:
    print("".join(bts))
    exit(0)
for s in bts:
    go.update(d[s])
go2=set(go)
for g in go:
    go2.update(d[g])
for g2 in sorted(go2):
    print(g2)
    
