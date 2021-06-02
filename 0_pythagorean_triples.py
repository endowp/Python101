s=int(input())
a=1
while a<(s/2):
    b=1
    while b<(s/2):
        c=s-a-b
        if c**2==(a**2)+(b**2):
            print("%s, %s, %s (because %s^2 + %s^2 = %s^2\
, and %s + %s + %s = %s)" %(a,b,c,a,b,c,b,a,c,s))
            exit(0)
        b+=1
    a+=1
print("No Triple")

        
