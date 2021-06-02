n=int(input())
namead={}
adname={}
adnum={}
for i in range(n):
    line=input().strip().split()
    namead[line[0]]=tuple(line[1:],)
n=int(input())
for i in range(n):
    line=input().strip().split()
    adname[line[0]]=tuple(line[2:],)
    adnum[line[0]]=int(line[1])
    
    
