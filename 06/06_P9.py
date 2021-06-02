books=[]
do=input()
while do != "end":
    if do[:6] == "return":
        books.append(do[7:])
        print(len(books))
    elif do == "shelf":
        if len(books) == 0:
            print("no book")
        else:
            pop = books.pop()
            print(pop)
    elif do == "top":
        if len(books) == 0:
            print("no book")
        else:
            print(books[-1])
    elif do == "list":
        print(books)
    do=input()
