n=int(input())
num=[]
new=[1]
j=1
for i in range(n):
    num.append([int(input()),j])
    j+=1
for number,index in num:
    k=1
    while k<n-1:
        if new[j-1]==index:
            new.append(number)
        k+=1
print(new)
        
