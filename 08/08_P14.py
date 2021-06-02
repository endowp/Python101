n=int(input())
dg={}     #group
di={}     #รุ่น
dd={}     #ภาค
t=()
namet=()
for i in range(n):
          info = input()
          t+=(info,)
          name, g, i, d = info.strip().split()
          namet+=(name, )
          if g not in dg:
                    dg[g] = {name}
          else:
                    dg[g].add(name)
          if i not in di:
                    di[i] = {name}
          else:
                    di[i].add(name)
          if d not in dd:
                    dd[d] = {name}
          else:
                    dd[d].add(name)
find = input().split()
intersec = namet
for f in find:
          if f in dg:
                    intersec = set(intersec) & dg[f]
          elif f in di:
                    intersec = set(intersec) & di[f]
          elif f in dd:
                    intersec = set(intersec) & dd[f]
          else:
                    intersec=()
if len(intersec)>0:   
          for subt in sorted(t):
                    for inter in intersec:
                              if inter == subt.split()[0]:
                                        print(subt)
else:
          print("Not Found")
