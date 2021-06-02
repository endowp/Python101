n=int(input())
d={}
temp=[]
for i in range(n):
    typ, word=input().split()
    temp.append(word)
    if word[:2] not in d:
        d[word[:2]]={word}
    else:
        d[word[:2]].add(word)
maxlen=0
for k,v in d.items():
    if len(v)>maxlen:
        maxlen=len(v)
        tw=k
        tempk=k[:2]
    elif len(v)==maxlen:
        if k[:2]<tempk:
            maxlen=len(v)
            tw=k
            tempk=k[:2]
print(tw)
print(maxlen)
for t in temp:
    for data in d[tw]:
        if data==t:
            print(data)
    
        
