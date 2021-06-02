d={}
while True:
    s=input().split()
    if s == ["-1"]:
        break
    else:
        id,subject=s[0],s[1:]
        for sub in subject:
            if sub not in d:
                d[sub]={id}
            else:
                d[sub].add(id)
class1,class2=input().split()
if (class1 in d) and (class2 in d):
    twoclass=len(d[class1] & d[class2])
    orclass=len(d[class1] | d[class2])
    oneclass=orclass-twoclass
elif class1 in d:
    twoclass=0
    orclass=oneclass=len(d[class1])
elif class2 in d:
    twoclass=0
    orclass=oneclass=len(d[class2])
else:
    twoclass=orclass=oneclass=0
print(twoclass,oneclass,orclass)
