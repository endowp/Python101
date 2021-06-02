import numpy as np
def mul(array,time): #เอาไว้คูณเมทริกซ์ array จน. time รอบ
    j=1
    while j <= time:
        array= array.dot(array)
        j+=1
    return array
n=int(input())
A=[]
for i in range(n):
    A.append([int(e) for e in input().split()])
A=np.array(A)
B=np.array(A)
for i in range(1,n):
    B = B+ mul(A,i)
    print(B)
for row in np.sign(B):
    for col in row:
        print(col, end=" ")
    print()
