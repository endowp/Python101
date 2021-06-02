import numpy as np
n=int(input())
L=[]
for i in range(n):
    L.append([int(e) for e in input().split()])
A=np.array(L)
for i in range(2): #ทำซ้ำ 2 รอบ
    for row in range(len(A)):
        for col in range(len(A)):
            if A[row][col] == 1:
                for k in range(len(A[col])): #ดูว่าคนี่รู้จักรู้จักใครบ้าง
                    if A[col][k] == 1:
                        A[row][k] = 1
for row in A:
    for r in row:
        print(r, end=" ")
    print()
