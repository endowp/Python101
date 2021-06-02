n = int(input())
listY=[]
listX=[]
for x in range(n):
    for y in range(n):
        if x**2 + y**2 == n:
            for i in listX:
                for j in listY:
                    if (x!=j) and (x!=i) and (y!=j) and (y!=i):
                        print(y, x)
            listY+=str(y)
            listX+=str(x)
print(listY)
print(listX)
