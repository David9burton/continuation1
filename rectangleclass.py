class Rectangle:
    def __init__(self, length=None, width=None):
        if length is None and width is None:
            self.length = float(input("Enter the length of the rectangle: "))
            self.width = float(input("Enter the width of the rectangle: "))
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle()
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

class Square(Rectangle):
    def __init__(self):
        side_length = float(input("Enter the side length of the square: "))
        super().__init__(side_length, side_length)

square = Square()
print(f"Area: {square.area()}")
print(f"Perimeter: {square.perimeter()}")
