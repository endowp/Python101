n=int(input())
count=1
tempPre=tempSuf=pre=suf= ""
i=k=m=0
for j in range(n):
    word=str(input())
    wordRe=word[::-1]
    if m==0:
        tempPre=word
        tempSuf=wordRe
        m+=1
    while i<len(word) and i<len(tempPre):
        if word[i]==tempPre[i]:
            pre+=word[i]
        else:
            break
        i+=1
    tempPre=pre
    if count<n:
        pre=""
    i=0
    while k<len(wordRe) and k<len(tempSuf):    
        if wordRe[k]==tempSuf[k]:
            suf+=wordRe[k]
        else:
            break
        k+=1
    tempSuf=suf
    if count<n:
        suf=""
    k=0
    count+=1
if pre !="":
    print(pre)
else:
    print("NO COMMON PREFIX")
if suf !="":
    print(suf[::-1])
else:
    print("NO COMMON SUFFIX")
