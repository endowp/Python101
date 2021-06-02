import numpy as np
price=[]
amount=[]
n=int(input())
for i in range(n):
    price.append(input().split("\t")[1])
for i in range(n):
    amount.append(input().split("\t")[1:])
npprice=np.array(price,int)
npamount=np.zeros([len(amount),len(amount[0])])
for i in range(len(amount)):
    npamount[i] = amount[i]
for i in np.dot(npprice,npamount):
    print(i)

    
