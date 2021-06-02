n=int(input())
subfac={}
facnisit={}
nisitfac={}
for i in range(n):
    subject, factory = input().strip().split(",")
    subfac[subject] = factory
n = int(input())
for i in range(n):
    subject, nisit =input().strip().split(",")
    if subject in subfac:
        if subfac[subject] not in facnisit:
            facnisit[subfac[subject]] = {nisit}
        else:
            facnisit[subfac[subject]].add(nisit)
        if nisit not in nisitfac:
            nisitfac[nisit] = {subfac[subject]}
        else:
            nisitfac[nisit].add(subfac[subject])
want = input().split(":")
d={}
new=dict(nisitfac)
for s in nisitfac:
    for ns in nisitfac[s]:
        if ns not in set(want):
          new[s] = new[s] - {ns}
o=0
for w in want:
    d[len(want)-o]=set()
    o+=1
for s in new:
    if len(new[s]) not in d:
        d[len(new[s])] = {s}
    else:
        d[len(new[s])].add(s)
m=0
for k,v in sorted(d.items(), reverse = True):
    if len(want)-m > 0:
        print("registered in",len(want)-m,"faculty:",len(v),"student")
        if len(v)>0:
            print("\n".join(sorted(v)))
        m+=1


