f=open(input())
file=f.readlines()
out=[]
names=[]
for s in file:
    fruit,name=s.split()
    if [fruit] not in out:
        out.append([fruit])
count=len(out)
for s in file:
    i=0
    names.append([])
    fruit,name=s.split()
    while i<count:
        if out[i]==[fruit]:
            names[i].append(name)
        i+=1
c=0
while c<len(names):
    if len(names[c])==0:
        del names[c]
    c+=1
d=j=0
most=0
temp=0
for o in out:
     o.append(names[d])
     if len(names[d])>temp:
         temp=len(names[d])
         most=o[0]
     d+=1
print(out)
print("The most favorite fruit is",most)
