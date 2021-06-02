flat=[]
def sumlist( x ):
    for sx in x:
        if type(sx)==list:
            flatting(sx)
        else:
            flat.append(sx)
    return sum(flat)
def flatting( x ):
    for sx in x:
        if type(sx)==list:
            flatting(sx)
        else:
            flat.append(sx)
print(sumlist(eval(input().strip()))) # do not remove this line 
