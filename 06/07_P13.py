data=[]
allinput=input()
while " " in allinput:
    subdata=allinput.split()
    data.append([subdata[0],float(subdata[1])])
    allinput=input()
data[-1]
print(data)    
