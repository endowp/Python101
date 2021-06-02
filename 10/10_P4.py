def h(n): # Tower of Hanoi
    if n==0:
        return 0
    else:
        return 2*h(n-1) +1
def gcd(x,y): # Greatest Common Divisor
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def J(n,k): # Josephus Problem
    if n==1:
        return 0
    else:
        return (J(n-1,k)+k)%n
def C(n): # Catalan Number
    if n>0:
        total=0
        for k in range(n):
            total+=C(k)*C(n-k-1)
        return total
    else:
        return 1
def f(n): # Fibonacci Number
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n%2==0:
        m=n/2
        return ((2*f(m-1))+f(m))*f(m)
    else:
        m=(n+1)/2
        return (f(m)**2) + (f(m-1)**2)
def F(n): # Female sequence
    if n==0:
        return 1
    else:
        return n-M(F(n-1))
def M(n): # Male sequence
    if n==0:
        return 0
    else:
        return n-F(M(n-1))
def A(m,n): # Ackermann Number
    if m==0:
        return n+1
    elif n==0:
        return A(m-1,1)
    else:
        return A(m-1,A(m,n-1))
exec(input().strip()) # do not remove this line
