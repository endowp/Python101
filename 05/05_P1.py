i=int(input())
part="D:\Endo\Python๑๐๑\score.txt"
file=open(part,"r")
for line in file:
    f=line.split()
    if int(f[0])==int(i):
        print(f[1])
        exit(0)
print("Not Found")
