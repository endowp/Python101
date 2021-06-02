s=input()
sLower=s.lower()
i=count=0
while i<len(s):
    if s[i]!=sLower[i]:
        count+=1
    i+=1
print(count)
