part="D:\Endo\Python๑๐๑\data.txt"
f=open(part,"r")
sec=int(input())
summ=0
n=num=0
for line in f:
    line=line.strip()
    start=line.find(":",11)
    stop=line.find(":",start+1)
    secf=line[start+1:stop]
    if sec==int(secf):
        findscore=line.find(":",stop)
        score=line[findscore+1:]
        n+=1
        summ+=float(score)
if n<=0:
    print("Not Found")
else:
    print(summ/n)
