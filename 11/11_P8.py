import numpy as np
def all_pair_distances(p):
    x = p[:, 0] # พิกัด x ของทุก p ซึ่งคือข้อมูลในทุกแถว คอลัมน์ที่ 0 ชอง p
    y = p[:, 1] # พิกัด x ของทุก p ซึ่งคือข้อมูลในทุกแถว คอลัมน์ที่ 1 ชอง p
    X = np.array([x]) # สร้างเมทริกซ์ขนาด 1*n จากข้อมูลพิกัด x
    Y = np.array([y]) # สร้างเมทริกซ์ขนาด 1*n จากข้อมูลพิกัด y
    dX = X-X.T # ให้ dX คือ X ลบด้วย transpose ของ X
    dY = Y-Y.T # ให้ dY คือ Y ลบด้วย transpose ของ Y
    d = ((dX**2) + (dY**2))**(0.5) # ค านวนระยะทางระหว่างทุกคู่จุดจากค่าของ dX กับ dY
    print("x = ", x)
    print("y = ", y)
    print("X = ", X)
    print("Y = ", Y)
    print("dX = ", dX)
    print("dY = ", dY)
    return d
exec(input().strip()) # do not remove this line
