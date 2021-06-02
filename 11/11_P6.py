import numpy as np
def checker(n):# หาวิธีเขียนอย่างมากสามค าสั่ง
    check=np.zeros([n,n],int)
    for i in range(n):
        if i%2==0:
            a=1
        else:
            a=0
        for j in range(a,n,2):
            check[i][j]=1
    return check
def collide(e,c):# หาวิธีเขียนอย่างมากสองค าสั่ง
    #collide formular >>> (x2-x1)^2 + (y1-y2)^2 <= (r1+r2)^2
    x=e[0]
    y=e[1]
    r=e[2]
    ans=[]
    for row in c:
        if  (x-row[0])**2 + (y-row[1])**2 <= (r+row[2])**2:
            ans.append(row)
    return np.array(ans)
def matrix_chain_mult(M, order):# อย่าลืมคูณตามล าดับที่ก าหนดใน order
    ans=M[order[0]]
    for o in order[1:]:
        print(M[o],ans)
        ans = np.multiply(M[o], ans)
    return ans
exec(input().strip()) # do not remove this line
