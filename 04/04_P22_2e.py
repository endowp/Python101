s=input()
num="0123456789"
eng=["zero","one","two","three","four","five","six","seven","eight","nine"]
count=2
for i in s:
    for n in num:
        if i==num[int(n)]:
            if count>2:
                print(" ",end="")
                count-=1
            if i==n:
                print(eng[int(n)],end="")
                count+=1
    if i=="-":
        count-=1
    if i ==" ":
        if count<2:
            count+=1
    if i not in num:
        if count>2:
            print(" ", end="")
            count=2
        print(i, end="")
