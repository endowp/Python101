s=input().replace(".","")
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
        if count>1:
            print(True)
            exit(0)
print(False)
    
