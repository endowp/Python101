choices={}
max_admitted={}
sorted_applicants={}
unassigned=[]
admitted={}
n=int(input())
for i in range(n):
    line=input().strip().split()
    unassigned.append(line[0])
    choices[line[0]]=tuple(line[1:])
n=int(input())
for i in range(n):
    line=input().strip().split()
    sorted_applicants[line[0]]=tuple(line[2:])
    max_admitted[line[0]]=int(line[1])
    admitted[line[0]]=[]
    print(admitted)
while len(unassigned)>0:
    sid=unassigned.pop()
    print(admitted)
    if len(choices[sid])>0:
        pid=choices[sid][0]
        choices[sid]=choices[sid][1:]
        print(admitted)
        admitted[pid].append(sid)
        if len(admitted[pid])>max_admitted[pid]:
            j=-1
            temp=sorted_applicants[pid][j]
            while temp not in admitted[pid] and j!=-len(admitted[pid]):
                j-=1
            else:
                if temp in admitted[pid]:
                    del admitted[pid][admitted[pid].index(temp)]
                    unassigned.append(temp)
               # break
for k,v in sorted(admitted.items()):
    print(k, end=" ")
    for sv in sorted(v) :
        print(sv,end=" ")
    print("")
