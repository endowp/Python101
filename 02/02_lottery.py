p1,p2,p3,n1,n2=[int(e) for e in input().split()]
#n1 n1 คือซื้อเลขn1ถึงn2 มี5หลัก ให้หาเงินรางวัลรวม
#p1 รางวัลที่1 ได้10000บาท
#p2 เลขท้าย2ตัว ได้25บ/เลข
#p3 เลขท้าย3ตัว ได้ 100บ/เลข
total=0
if n1<=p1<=n2:
    total+=10000
while n1<=n2:
    n1=str(n1)
    if int(n1[-2:])==p2:
        total+=25
    if int(n1[-3:])==p3:
        total+=100
    n1=int(n1)
    n1+=1
print(total)
