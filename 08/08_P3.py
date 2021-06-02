file=open("address.txt")
d={}
for line in file:
    name,sur,number=line.strip().split()
    d[name,sur]=number
while True:
    find = input().strip().split()
    if len(find) > 1:
        na,su=find
        if (na,su) in d:
            print(d[na,su])
        else:
            print("Not Found")
    elif len(find) == 1:
        if find[0] in d.values():
            for key,value in d.items():
                if find[0]==value:
                    print(key[0],key[1])
        else:
            print("Not Found")
    else:
        break
        
    
