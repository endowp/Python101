def PM(a,k,m):
    if k==0:
        return 1
    elif k%2==0:
        return ( (  ( a**(k//2) ) % m  )**2 ) % m
    else:
        return a* ( (  ( a**(k//2) ) % m  )**2 ) % m
a, k, m = [int(e) for e in input().split()]
print(PM(a, k ,m))
