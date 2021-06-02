lp={} #key = liker, value = poster
pl={} #key = poster, value = liker
while True:
    line = input().split()
    if line == ["done"]:
        break
    else:
        liker = line[0]
        poster = line[1:]
        lp[liker] = poster
        for p in poster:
            if p not in pl:
                pl[p] = {liker}
            else:
                pl[p].update(liker)
char = input().split()
if char == ["R"]:
    for subl in sorted(lp):
        print(subl, len(lp[subl]))
elif char == ["T"]:
    maxliked = []
    numlike = 0
    for subp in pl:
        if len(pl[subp]) > numlike:
            maxliked = [subp]
            numlike = len(pl[subp])
        elif len(pl[subp]) == numlike:
            maxliked += [subp]
    if len(maxliked) > 0:
        for ml in sorted(maxliked):
            print(ml)
    else:
        print("None")
elif char[0] == "C":
    if char[1] not in pl or char[2] not in pl:
        print("None")
    else:
        l2people = pl[char[1]] & pl[char[2]]
        if len(l2people) > 0:
            for l2p in sorted(l2people):
                print(l2p)
        else:
            print("None")
elif char == ["M"]:
    mutual=[]
    for key in pl:
        for value in pl[key]:
            if value in pl and key in pl[value]:
                mutual.append( tuple((value,key)))
                mutual.append(tuple((key, value)))
    if len(mutual) > 0:
        for m in sorted(set(mutual)):
            print(m)
    else:
        print("None")
