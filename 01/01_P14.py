num=input()
count=13
x=0
n=0
for i in str(num):
    while count>=2:
        x+=int(num[n])*count
        n+=1
        count-=1
print((11-(x%11))%10)
