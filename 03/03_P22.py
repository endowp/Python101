l=int(input())
a=1
maxL=1
while a<l/2:
    b=1
    while b<l/2:
        c=l-(a+b)
        if (a**2)+(b**2)==c**2:
            if (c>=a) and (c>=b) and (c>=maxL):
                maxL=c
           # if (a>=b) and (a>=c) and (a>=maxL):
             #   maxL=a
            #elif  (b>=a) and (b>=c) and (b>=maxL):
               # maxL=b
            #elif (c>=a) and (c>=b) and (c>=maxL):
              #  maxL=c
        b+=1
    a+=1
print(maxL)
