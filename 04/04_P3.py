s=str(input())
vowel=0
conso=0
s=s.lower()
for i in s:
    if i == "a" or i=="e" or i=="i"  or i=="o" or i=="u":
        vowel+=1
    elif i=="b" or i=="c" or i=="d" or i=="f" or i=="g" or i=="h" or i=="j" or i=="k"\
         or i=="l" or i=="m" or i=="n" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" \
         or i=="v" or i=="w" or i=="x" or i=="y" or i=="z":
        conso+=1
print(vowel, conso)
