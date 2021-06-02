from operator import itemgetter
n=int(input())
locationf={}
agef={}
for i in range(n):
    code, age, status, location = input().strip().split(",")
    if location not in locationf:
        locationf[location] = 1
    else:
        locationf[location] += 1
    if int(age) not in agef:
        agef[int(age)] = 1
    else:
        agef[int(age)] += 1
one, two, three = input().strip().split(",")
if one == "P":
    ans = locationf
elif one == "A":
    ans = agef
if three == "ASC":
    ans=sorted(ans.items())
elif three == "DSC":
    ans=sorted(ans.items(),reverse=True)
if two == "ASC":
    ans=sorted(ans,key=itemgetter(1))
elif two =="DSC":
    ans=sorted(ans,key=itemgetter(1),reverse=True)
for a in ans:
    for suba in a:
        print(suba, end=" ")
    print()
