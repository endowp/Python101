s=input()
code1=input()
code2=input()
for i in s:
    n=0
    count=0
    while n<len(code1):
        if i==code1[n]:
            print(code2[n], end="")
            count+=1
        elif i==code2[n]:
            print(code1[n], end="")
            count+=1
        n+=1
    if count==0:
        print(i,end="")

