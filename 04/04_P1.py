s=str(input())
for i in s:
    if i=="\"" or i=="'" or i=="," or i=="." or i=="(" or i==")":
        print(" ", end="")
    else:
        print(i, end="")
