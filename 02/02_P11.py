Aa,Va=input().split()
Ab,Vb=input().split()
Aa,Va,Ab,Vb=int(Aa),int(Va),int(Ab),int(Vb)
Fb=Ab-Vb
while Fb>0 and Va>0:
    Vb+=1
    Va-=1
    Fb-=1
print(Va,Vb)
