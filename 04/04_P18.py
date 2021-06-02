s=input()
s=s.lower()
group=0
j=0
for i in s:
    j+=1
    if j<len(s):
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            if s[j] !="a" and s[j] !="e" and s[j] !="i" and s[j] !="o" and s[j] !="u":
                group+=1
    elif j==len(s):
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            group+=1
print(group)
