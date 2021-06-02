row=[]
row.append([int(e) for e in input().split()])
lenR=len(row[0])
r=int((lenR+1)/2)-1
# from lenR=(2*r)-1 แล้วหักออก1บรรทัด
for i in range(r):
    row.append([int(e) for e in input().split()])
sumnum=0
i=int(lenR/2)
j=i+1
for subrow in row:
    sumnum+=sum(subrow[i:j])
    i-=1
    j+=1
print(sumnum)
