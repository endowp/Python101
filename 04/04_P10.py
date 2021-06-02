s=str(input())
s=s.lower()
newS=""
S1=""
S2=""
for i in s:
    if i !=" ":
        newS+=i
a=0
while a<len(newS)/2:
    S1+=newS[a]
    a+=1
b=len(newS)
while b>len(newS)/2:
    S2+=newS[b-1]
    b-=1
if S1==S2:
    print("yes")
else:
    print("no")
