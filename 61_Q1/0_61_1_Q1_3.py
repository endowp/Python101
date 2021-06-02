t=""
num=[]
row=[]
rc=[]
r=1
for i in range(9):
    t+=input()
count=0
for k in t:
    if count==9:
        num=[]
        count=0
        r+=1
    if k in num and r not in rc:
        #row.append(k)
        print(k,num,r,rc)
        rc.append(r)
    #print(num)
    num.append(k)
    count+=1
count=0
colCheck=[]
col=[]
for m in t:
    #print(colCheck,m)
    if m in colCheck and m not in col:
        col.append(m)    
    if count==0:
        colCheck=[]
        colCheck.append(m)
    if count==8:
        count=-1
    count+=1
#for n in row:
#    print(n,end="")
#print(col,end="")
for r in rc:
    print(r,end=" ")
