n=int(input())
count=n
sumnum=0
if n==0:
    print("No Data")
else:
    while count>0:
        num=float(input())
        sumnum+=num
        count-=1
    print(sumnum/n)
    
