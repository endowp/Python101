t=[]
num=[]
ansRow=ansCol=ansBox=[]
rc=[]
r=1
for i in range(9):
    t.append(input())
row=1
for st in t: #ansRow
    for j in range(1,10):
        k=st.find(str(j))
        if k==-1:
            ansRow.append(row)
            break
    row+=1
n=0
while n<=8: #ansCol
    m=0
    c=""
    while m<=8:
        c+=t[m][n]
        m+=1
    for x in range(1,10): 
        cf=c.find(str(x))
        if cf==-1:
            ansCol.append(n+1)
            break
    n+=1

#ansBox
box1=str(t[0][0])+str(t[0][1])+str(t[0][2])+str(t[1][0])+str(t[1][1])+str(t[1][2])\
       +str(t[2][0])+str(t[2][1])+str(t[2][2])
box2=str(t[0][3])+str(t[0][4])+str(t[0][5])+str(t[1][3])+str(t[1][4])+str(t[1][5])\
       +str(t[2][3])+str(t[2][4])+str(t[2][5])
box3=str(t[0][6])+str(t[0][7])+str(t[0][8])+str(t[1][6])+str(t[1][7])+str(t[1][8])\
       +str(t[2][6])+str(t[2][7])+str(t[2][8])
box4=str(t[3][0])+str(t[3][1])+str(t[3][2])+str(t[4][0])+str(t[4][1])+str(t[4][2])\
       +str(t[5][0])+str(t[5][1])+str(t[5][2])
box5=str(t[3][3])+str(t[3][4])+str(t[3][5])+str(t[4][3])+str(t[4][4])+str(t[4][5])\
       +str(t[5][3])+str(t[5][4])+str(t[5][5])
box6=str(t[3][6])+str(t[3][7])+str(t[3][8])+str(t[4][6])+str(t[4][7])+str(t[4][8])\
       +str(t[5][6])+str(t[5][7])+str(t[5][8])
box7=str(t[6][0])+str(t[6][1])+str(t[6][2])+str(t[7][0])+str(t[7][1])+str(t[7][2])\
       +str(t[8][0])+str(t[8][1])+str(t[8][2])
box8=str(t[6][3])+str(t[6][4])+str(t[6][5])+str(t[7][3])+str(t[7][4])+str(t[7][5])\
       +str(t[8][3])+str(t[8][4])+str(t[8][5])
box9=str(t[6][6])+str(t[6][7])+str(t[6][8])+str(t[7][6])+str(t[7][7])+str(t[7][8])\
       +str(t[8][6])+str(t[8][7])+str(t[8][8])
for q1 in range(9):
    w=box1.find(str(q1))
    if w==-1:
        ansBox.append(1)
        break
for q2 in range(9):
    w=box2.find(str(q2))
    if w==-1:
        ansBox.append(2)
        break
for q3 in range(9):
    w=box3.find(str(q3))
    if w==-1:
        ansBox.append(3)
        break
for q4 in range(9):
    w=box4.find(str(q4))
    if w==-1:
        ansBox.append(4)
        break
for q5 in range(9):
    w=box5.find(str(q5))
    if w==-1:
        ansBox.append(5)
        break
for q6 in range(9):
    w=box6.find(str(q6))
    if w==-1:
        ansBox.append(6)
        break
for q7 in range(9):
    w=box7.find(str(q7))
    if w==-1:
        ansBox.append(7)
        break
for q8 in range(9):
    w=box8.find(str(q8))
    if w==-1:
        ansBox.append(8)
        break
for q9 in range(9):
    w=box9.find(str(q9))
    if w==-1:
        ansBox.append(9)
        break
ty=input()
if ty=="R":
    print("Row: ",end="")
    if ansRow=="":
        print("OK")
    else:
        for aa in ansRow:
            print(aa, end=" ")
elif ty=="C":
    print("Col: ",end="")
    if ansCol=="":
        print("OK")
    else:
        for bb in ansCol:
            print(bb, end=" ")
elif ty=="B":
    print("Box: ",end="")
    if ansBox=="":
        print("OK")
    else:
        for v in ansBox:
            print(v,end=" ")
else:
    print("Row: ",end="")
    if ansRow=="":
        print("OK")
    else:
        for d in ansRow:
            print(d, end=" ")
    print("")
    print("Col: ",end="")
    if ansCol=="":
        print("OK")
    else:
        for f in ansCol:
            print(f, end=" ")
    print("")
    print("Box: ",end="")
    if ansBox=="":
        print("OK")
    else:
        for g in ansBox:
            print(g,end=" ")
