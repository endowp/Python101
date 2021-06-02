def GCD(x,y):
    if x>=y and x%y==0:
        return y
    else:
        return GCD(y,x%y)
x,y =[int(e) for e in input().split()]
print(GCD(x,y))
