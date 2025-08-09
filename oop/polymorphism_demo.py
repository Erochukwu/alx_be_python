import math

class Shape:
    def area(self):
        print("NotImplementedError")

class Retangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        area = length * width
        return area

class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        area = math.pi * (self.radius ** 2)
        return area