f=open(input())
stulist=[]
stu=[]
grade=[]
for line in f:
    line=line.strip()
    stulist+=[line.split(";")]
for s in stulist:
    score=float(s[3])+float(s[4])
    if score>=80:
        grade.append("A")
    elif score>=70:
        grade.append("B")
    elif score>=60:
        grade.append("C")
    elif score>=50:
        grade.append("D")
    else:
        grade.append("F")
i=0
for s in stulist:
    stu+=[[s[0],s[1]+" "+s[2],grade[i]]]
    i+=1
print(stu)
