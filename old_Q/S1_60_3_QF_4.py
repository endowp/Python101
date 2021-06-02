card=input().strip().split()
do = list(input().strip().replace(" ",""))
for d in do:
    s1=card[:int(len(card)/2)] #ครึ่งแรก
    s2=card[int(len(card)/2):] #ครึ่งหลัง
    if d == "C":
        card=s2+s1
    elif d== "S":
        card=[]
        i=0
        while i<len(s1):
            card.append(s1[i])
            card.append(s2[i])
            i+=1
for c in card:
    print(c, end=" ")
