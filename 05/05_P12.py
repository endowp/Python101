part1=input()
part2=input()
f1=open(part1)
f2=open(part2)
for line in f1:
    r=int(line)
    n=r
    av=0
    while r>0:
        a=f2.readline()
        av+=float(a)
        r-=1
    print(av/n)
        
        
