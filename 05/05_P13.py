part=input()
n=int(input())
letter1=input()
letter2=input()
newline=""
f=open(part)
for line in f:
    newline=line.upper()
    found=newline.find(letter1.upper())
    while found>0 and n>0:
        print(line[:found],end="")
        print(letter2,end="")
        found=newline.find(letter1.upper(),found)
            #print(line[len(line)-found-len(letter1)-len(letter2):],end="")
        #print(line[len(letter1)+found:],end="")
        n-=1
    else:
        print(line[found+len(letter1):])
#for line in file:
#   print(line,end="")
