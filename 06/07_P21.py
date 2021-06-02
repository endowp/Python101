file=open("circulations.txt")
date=int(input().strip())
datebook=[]
for line in file:
    book,member,due=line.strip().split()
    if int(due)<date:
        datebook.append(line.strip())
i=0
while i<len(datebook)-1:
    j=0
    while j<len(datebook)-1:
        start1=datebook[j].find(" ",(datebook[j].find(" ")+1))
        start2=datebook[j+1].find(" ",(datebook[j+1].find(" ")+1))
        if (datebook[j][start1+1:])>(datebook[j+1][start2+1:]):
            datebook[j],datebook[j+1] = datebook[j+1], datebook[j]
        j+=1
    i+=1
if len(datebook)>0:
    for d in datebook:
        print(d)
else:
    print("Not Found")
file.close
