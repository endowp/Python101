class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def area(self):
         dx = upperright.x - lowerleft.x
         dy = upperright.y - lowerleft.y
         return dx * dy
    def contains(self,p):
        if lowerleft.x <= p.x <= upperright.x  \
            and lowerleft.y <= p.y <= upperright.y :#check x & y
            return True
        return False
x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(Rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(Rect.contains(p))
