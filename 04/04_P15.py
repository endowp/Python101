s=str(input())
s=s.lower()
count=0
temptC=0
tempt=""
for i in s:
    if i==tempt:
        count+=1    
    elif i !=tempt:
        tempt=i
        count=1
    if count>temptC:
        temptC=count
print(temptC)
