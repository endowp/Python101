text=str(input())
s1=str(input())
s2=str(input())
newText=""
for i in text:
    if i==s1 :
        newText+=s2
    elif i==s2:
        newText+=s1
    else:
        newText+=i
print(newText)
        
