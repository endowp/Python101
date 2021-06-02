isbn=input()
count=10
num=0
n=0
for i in isbn:
    while count>=2:
        num+=int(isbn[n])*count
        count-=1
        n+=1
for j in range(0,10):
    if ((num+j)%11)==0:
        print (str(isbn)+str(j))

