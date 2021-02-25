#area of a triangle
class Triangle():
    def __init__(self, base, height):
        self.b = base
        self.h = height

    def Area(self):
        area = 0.5*self.b*self.h
        return area



T1 = Triangle(10, 4)

print(T1.Area())