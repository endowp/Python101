n=int(input())
win=set()
lose=set()
for i in range(n):
    w,l=input().split()
    win.add(w)
    lose.add(l)
nolose=win-lose
print(sorted(nolose))
