def tiling(x, c): # คืนค่าจ้านวนวิธีการปูกระเบื้อง x แผ่น โดยที่แผ่นสุดท้ายเป็นสี c
# กรณีปู 1 แผ่น ได้ว่ามีวิธีการปูกระเบื้อง 1 วิธี
    if x == 1: return 1
# กรณีปูมากกว่า 1 แผ่น ให้ค้านวณแบบ recursive
    else:
        way=""
        ways={}
        way=way[:]+c
        if len(way)==N:
            ways.add(way)
        elif c=="G":
            tiling(x, "R")
            tiling(x, "B")
        else:
            tiling(x,"G")
            tiling(x, "R")
            tiling(x, "B")
    return len(ways)
N = int(input())
print(tiling(N,'G')+tiling(N,'R')+tiling(N,'B'))
