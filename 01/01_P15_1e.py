h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
if h2>=h1:
    if t1>t2:
        dt=t1-t2
    else:
        dt = t2 - t1
    dh = dt // (60*60)
else:
    dt=t2+(24*60*60)-t1
    dh=24+(h2-h1)
dt -= dh * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
print(str(dh)+":"+str(dm)+":"+str(ds))
