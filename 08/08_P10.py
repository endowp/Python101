num=int(input())
dname={}
did={}
saw=[]
sortid=[]
for i in range(num):
    id,name=input().split(":")
    sortid.append(id)
    for n in name.strip().split(", "):
        if n not in dname:
            dname[n]={id}
        else:
            dname[n].add(id)
    if id not in did:
        did[id]={name.strip()}
    else:
        did[id].add(name.strip())
see=input().strip()
if see in did:
    for vdid in did[see]:
        for v in vdid.strip().split(", "):
            for sub in dname[v]:
                if sub != see and sub not in saw:
                    saw.append(sub)
if len(saw)>0:
    for sid in sortid:
        for s in saw:
            if sid==s:
                print(s)
else:
    print("Not Found")
