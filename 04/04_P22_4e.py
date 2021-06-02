s=input()
num="0123456789"
eng=["zero","one","two","three","four","five","six","seven","eight","nine"]
n=0
nn=0
while n<len(s):
    while nn<len(num):
        if str(num[nn]) == str(s[n]) and (s[n+1] in num):
            print(eng[n], end=" ")
        elif num[nn]==s[n] and (s[n+1]=="-"):
            print(eng[n],end="")
        elif num[nn]==s[n]:
            print(eng[n],end="")
        nn+=1
    n+=1
        
    if s[n] not in num:
        print(s[n],end="")
        n+=1
