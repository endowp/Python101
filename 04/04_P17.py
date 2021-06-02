s=input()
temp=""
for i in s:
    for j in s:
        count=0
        if j==i and count==1:
            print(j, end="")
        count+=1
