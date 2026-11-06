# Worksheet 1.5: Rectangle Class
import sys

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")

        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Both parameters must be integers")

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """Returns true if its a rectangle or false if it isn't"""
        return self.width == self.height
    
    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


rectangle = Rectangle(5, 10)

print(rectangle.is_square())  # False
print(rectangle.area())       # 50
print(rectangle.perimeter())  # 30

square = Rectangle(5, 5)

print(square.is_square())
    
#Rectangle("5", 10)  # Raises TypeError
#Rectangle(5, 0)     # Raises ValueError
#Rectangle(-2, 5)
