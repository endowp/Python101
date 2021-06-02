part=input()
f=open(part)
n=i=0
for line in f:
    summ=0
    if n>0:
            start1=line.find(" ")
            stop1=line.find(" ",start1+1)
            summ+=int(line[start1+1:stop1+1])
            
            start2=line.find(" ",stop1)
            stop2=line.find(" ",start2+1)
            summ+=int(line[start2+1:stop2+1])
            
            start3=line.find(" ",stop2)
            stop3=line.find(" ",start3+1)
            summ+=int(line[start3+1:stop3+1])
            
            start4=line.find(" ",stop3)
            stop4=line.find(" ",start4+1)
            summ+=int(line[start4+1:stop4+1])
            
            start5=line.find(" ",stop4)
            stop5=line.find(" ",start5+1)
            summ+=int(line[start5+1:])
            if summ>=80:
                grade="A"
            elif summ>=75:
                grade="B+"
            elif summ>=70:
                grade="B"
            elif summ>=65:
                grade="C+"
            elif summ>=60:
                grade="C"
            elif summ>=55:
                grade="D+"
            elif summ>=50:
                grade="D"
            else:
                grade="F"
            nisit=line.find(" ")
            print(line[:nisit],grade)
    n+=1
