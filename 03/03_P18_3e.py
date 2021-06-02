n = int(input())
count=2
prime=[]
primeFac=[]
while n >=count:
    if n%count==0:
        prime.append(count)
    count2=2
    for i in prime:
        while count2<i:
            if (i%count2!=0):
                if ((i in primeFac)==False):
                    primeFac.append(i)
            count2+=1
    count+=1
for m in primeFac:
    print(m,end=" ")
            
 
