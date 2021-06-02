import numpy as np
def fib(n,k):
    A=np.array([[0, 1], [1, 1]])
    for i in range(n-1):
        A = (A.dot(A)) %k
    return A
n,k=[int(e) for e in input().split()]
print(fib(n,k))
