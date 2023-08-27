class Rectangle:
    def __init__(self):
        self.lenght = float(input("Enter the lenght of the rectangle: "))
        self.width = float(input("Enter the wifth of the rectangle: "))

    def area(self):
        return self.lenght * self.width
    
    def perimeter(self):
        return 2 * (self.lenght + self.widht)

rect = Rectangle()
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter}")
