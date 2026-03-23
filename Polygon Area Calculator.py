class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  

rect = Rectangle(10, 5)
square = Square(4)

print("Rectngle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())