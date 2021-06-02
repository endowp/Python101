t=[]
num=[]
row=[]
rc=[]
r=1
for i in range(9):
    t.append(input())
row=1
for st in t:
    for j in range(1,10):
        k=st.find(str(j))
        #if k==-1:
            #print(row,end=" ")
    row+=1
c=0
sc=0
#for st in t:
#    crow=1
#    while crow<=9 and c<=9:
#        cc=[]
#        if st[sc] == st[c] and crow not in cc:
#            cc.append(crow)
#        c+=1
#        crow+=1
#        print(cc,sc)
#    sc+=1
#col=0
#for st in t:
#    while col<9:
        
#    col+=1
col=""
rrow=1
while rrow<=9:
    n=0
    col=""
    while n<9:
        col+=t[n]
        print(col)
        if n==8:
            for a in range(1,10):
                b=col.find(str(a))
                #if b==-1:
                    #print(rrow)

        n+=1
    rrow+=1
        
