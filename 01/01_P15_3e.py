h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
if t1>t2:
    if h2==h1:
        if m1==m2:
            if s1>s2:
                dt=60*60*24+(s2-s1)
                dh = dt // (60*60)
                dt-=dh*60*60
                dm=dt//60
                dt-=dm*60
                ds=dt
            else: #s2>=s1
                dt=0
                dm=0
                ds=s2-s1
        else: #m1>m2
            dt=60*60*24+(t2-t1)
            dh=23
            dt-=dh*60*60
            dm=dt//60
            dt-=dm*60
            ds=dt            
    else: #h1>h2
        dh=0
        dm=0
        dt=24*60*60+(t2-t1)
        while dt>=60:
            dm+=dt//60
            dt-=60
            ds=dt
            while dm>=60:
                dh+=dm//60
                dt-=60
                ds=dt
else:
    dt=t2-t1
    dh=dt//(60*60)
    dt -= dh * 60*60
    dm = dt // 60
    dt -= dm*60
    ds = dt
print(str(dh)+":"+str(dm)+":"+str(ds))
