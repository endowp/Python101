i=1
total_stroke=0
handicap=18
point=0
while i<=9:
    par,stroke=[int(e) for e in input().split()]
    total_stroke+=stroke
    if stroke<=par:
        point+=2
        handicap-=2
    elif stroke<=par+1:
        point+=1
        handicap-=1
    i+=1
print(total_stroke)
print(handicap)
print(total_stroke-handicap)

