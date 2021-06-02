num=int(input())
numlist=[]
for i in range(1,num+1):
    numlist.append(i)
while True:
    swap=input().split()
    if swap[0] =="0" and swap[1] == "0":
        print(numlist)
        break
    else:
        s1=numlist.index(int(swap[0]))
        s2=numlist.index(int(swap[1]))
        if s1 !=-1 and s2!=-1:
            numlist[s1], numlist[s2] = numlist[s2], numlist[s1]
    
