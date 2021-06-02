d={}
n=int(input())
for i in range(n):
    num=int(input())
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
mincount=max(d.values())
dmax={}
for key,value in d.items():
    if value==mincount:
        dmax[key]=value
print(min(dmax))
    
