s1=str(input())
s2=str(input())
S1=s1.lower()
S2=s2.lower()
newS1=""
newS2=""
for i in S1:
    if i!=" ":
        newS1+=i
for j in S2:
    if j!=" ":
        newS2+=j
newS1=list(newS1)
newS2=list(newS2)
n=0
while n<=(len(newS1)-1):
    m=0
    while m<=(len(newS2)-1):
        if newS1[n]==newS2[m]:
            newS1.pop(n)
            newS2.pop(m)
            if m>=0:
                m-=1
            if n>=0:
                n-=1
            if (newS1==[] and newS2!=[]) or (newS1!=[] and newS2==[]):
                print(s1, s2)
                break
            elif newS1==[] and newS2==[]:
                print(s1)
        m+=1
    n+=1
if newS1!=[] and newS2!=[]:
    print(s1, s2)
