import math
x=int(input())
x=math.radians(x%360)
sinX=k=0
while k<10:
    sinX+=((-1)**k)*(((x**((2*k)+1))/math.factorial((2*k)+1)))
    k+=1
print(sinX)
