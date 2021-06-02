N,nf=input().split()
N=int(N)
nf=int(nf)
count=0
while N>0:
    n=int(input())
    if n==nf:
        count+=1
    N-=1
print(count)
