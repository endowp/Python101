part=input()
f=open(part)
BE=SE=VE=ET=0
for line in f:
    stop=line.find(" ")
    if stop==-1:
        stop=line.find("\t")
    ingre=line[:stop]
    if ingre.upper()=="BE":
        BE+=1
    elif ingre.upper()=="SE":
        SE+=1
    elif ingre.upper()=="VE":
        VE+=1
    elif ingre.upper()=="ET":
        ET+=1
print(BE,SE,VE,ET,BE+SE+VE+ET)
