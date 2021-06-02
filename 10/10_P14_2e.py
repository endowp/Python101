def tiling(x, c):
 # คืนค่าจ้านวนวิธีการปูกระเบื้อง x แผ่น โดยที่แผ่นสุดท้ายเป็นสี c
 # กรณีปู 1 แผ่น ได้ว่ามีวิธีการปูกระเบื้อง 1 วิธี
    if x == 1: return 1
 # กรณีปูมากกว่า 1 แผ่น ให้ค้านวณแบบ recursive
    else:
        return 3*( (N**2)-1 ) - (N-1)
 # write your code here
N = int(input())
print(tiling(N,"R"))
