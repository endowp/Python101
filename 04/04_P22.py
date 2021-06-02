s=input()
j=0
for i in s:
    j+=1
    if j>0:
        if s[j-1] !=" ":
            print(" ", end="")
        if i=="1":
            print("one",end="")
        elif i=="2":
            print("two", end="")
        elif i=="3":
            print("three", end="")
        elif i=="4":
            print("four", end="")
        elif i=="5":
            print("five", end="")
        elif i=="6":
            print("six", end="")
        elif i=="7":
            print("seven", end="")
        elif i=="8":
            print("eight", end="")
        elif i=="9":
            print("nine", end="")
        elif i=="0":
            print("zero", end="")
        else:
            print(i, end="")
