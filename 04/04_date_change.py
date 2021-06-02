date=input().replace("/","")
monthA=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG"\
        ,"SEP","OCT","NOV","DEC"]
day=date[2:4]
month=int(date[0:2])
year=date[4:8]
if int(month)<10:
    month=str(month).replace("0","")
print(day,monthA[int(month)-1],year)
