def x(n): # Logistic Map
    x=[0.01]
    for i in range(n):
        x.append(3*x[i]*(1-x[i]))
    return x[n]
def M(n): # Motzkin number
    if n==0 or n==1:
        return 1
    else:
        summ=0
        for k in range(n-1):
            summ+=M(k)*M(n-2-k)
        return M(n-1)+summ
def D(m,n): # Delannoy number
    if m==0 or n==0:
        return 1
    else:
        return D(m-1, n) + D(m-1, n-1) + D(m, n-1)
def S(n): # Schroder-Hipparchus number
    if n==1 or n==2:
        return 1
    else:
        return (1/n)*((6*n-9)*S(n-1)-(n-3)*S(n-2))
def d(n): # Number of Derangements
    if n==0:
        return 1
    else:
        return n*d(n-1) + (-1)**n
exec(input().strip()) # do not remove this line
