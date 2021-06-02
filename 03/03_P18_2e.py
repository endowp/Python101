n = int(input())
count=2
primeCount=0
#count2=n-1
prime=""
primeFac=""
while n>=count:
    if n%count==0:
        prime+=str(count)
        print("prime+= ",count)
    count+=1
for i in range(len(prime)):
    c=0
    print(i[c+1])
    if (i[c+len(prime)])%(i[c])==0:
        primeFac+=str(i)
        print("primeFac+= ",prime)
        primeCount+=1
    c-=1
if n>1:
    if primeCount==0:
        print("primeCount+= ",primeCount)
for j in primeFac:
    print("Ans: ",j)

            
 
