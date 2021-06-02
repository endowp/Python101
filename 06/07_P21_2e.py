file=open("circulations.txt")
data=[]
date=int(input())
for line in file:
    [book,member,due]=line.strip().split()
    if date>int(due):
            data.append([book,member,due])
i=0
while i<len(data)-1:
    j=0
    while j<len(data)-1:
        if int(data[j][2])>int(data[j+1][2]):
             data[j], data[j+1] = data[j+1], data[j]
        j+=1
    i+=1
if len(data)>0:
    for d in data:
        print(" ".join(d))
else:
    print("Not Found")
file.close
