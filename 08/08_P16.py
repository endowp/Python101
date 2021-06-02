n=int(input())
numdepart={} #k=depart, v=จำนวนรับ
for i in range(n):
    depart, numnisit = input().strip().split()
    numdepart[depart] = int(numnisit)
n=int(input())
tid=()
scoreid={} #k=score, v=id
dscore={} #k=score, v=department
for i in range(n):
    id, score, d1, d2, d3, d4 = input().strip().split()
    tid += (id, )
    dscore[float(score)] = (d1, d2, d3, d4)
    scoreid[float(score)] = id
departed={}
dscore=sorted(dscore.items(), reverse=True)
for s,d in dscore:
    for v in d:
        if numdepart[v]>0:
            departed[scoreid[s]]= v
            numdepart[v]-=1
            break
for k in sorted(departed):
    print(k, departed[k])
