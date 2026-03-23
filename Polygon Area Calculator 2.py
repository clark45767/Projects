
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return "Area not defined"

    def perimeter(self):
        return "Perimeter not defined"

    def display(self):
        print(f"Shape: {self.name}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


rect = Rectangle(10, 5)
square = Square(4)

rect.display()
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

print()

square.display()
print("Area:", square.area())
print("Perimeter:", square.perimeter())