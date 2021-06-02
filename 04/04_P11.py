s=str(input())
count=0
for i in s:
    if i=="1":
        count+=1
if count%2==0:
    s+="0"
else:
    s+="1"
print(s)
