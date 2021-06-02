dna=input()
t=input()
dna=dna.strip()
t=t.strip()
dna=dna.upper()
t=t.upper()
R=""
c=0
for i in dna:
    if i!="A" and i!="T" and i!="G" and i!="C":
        print("Invalid DNA")
        c=1
if t=="R" and c==0:
    for i in dna:
        if i=="A":
            R+="T"
        elif i=="T":
            R+="A"
        elif i=="G":
            R+="C"
        elif i=="C":
            R+="G"
    print(R[::-1])
elif t=="F" and c==0:
    countA, countT, countG, countC=0,0,0,0
    for i in dna:
        if i=="A":
            countA+=1
        elif i=="T":
            countT+=1
        elif i=="G":
            countG+=1
        elif i=="C":
            countC+=1
    print("A=%d, T=%d, G=%d, C=%d "%(countA, countT, countG, countC))
elif t=="D" and c==0:
    d=input()
    d1=d[0]
    d2=d[1]
    count=0
    s=1
    for i in dna:
        if i==d1:
           if dna[s]==d2:
               count+=1
        s+=1
    print(count)
