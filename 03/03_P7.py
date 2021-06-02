import math
x=float(input())
cosxn,cosx=1,0.0
k=0
while (cosxn>=10**-8)or(-1*cosxn>=10**-8):
    cosxn=(((-1)**k)*(x**(2*k)))/(math.factorial(2*k))
    cosx+=cosxn
    k+=1
print(cosx,k-2)
