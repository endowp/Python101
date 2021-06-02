s,sn=[str(e) for e in input().split()]
sumnum=0
news=""
count=0
for k in s:
    if count==0:
        news+=k.upper()
        count+=1
    else:
        news+=k.lower()
for j in sn:
    if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" \
       or j=="6" or j=="7" or j=="8" or j=="9":
        sumnum+=int(j)
print(news, sumnum)
