i=int(input())
n=2
while n<=i:
    if i%n==0:
        n2=2
        count=0
        while n2<n:
            if n%n2==0:
              count+=1  
            n2+=1
        if count==0:
            print(n, end=" ")
    n+=1
