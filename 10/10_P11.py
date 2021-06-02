def isSorted(L):
     if len(L)<=2:
         return True
     for i in range(1,len(L)-1):
         if not(L[i-1]<=L[i]<=L[i+1]) and not(L[i-1]>=L[i]>=L[i+1]):
             return False
     return True

n = int(input())
L = [int(e) for e in input().split()]
if isSorted(L):
     print('true')
else:
     print('false')
