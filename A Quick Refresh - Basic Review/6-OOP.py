class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width

    # @property
    # def width(self):
    #     print("Getting width")
    #     return self._width
    #
    # @property
    # def height(self):
    #     return self._width

    def __str__(self):
        return f"Rectangle: width={self._width}, height={self._height}"

    def __rep__(self):
        return f"Rectangle: {self._width}, {self._height}"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
print(r1._width)
print(r1.area())
print(r1.perimeter())
print(str(r1))
print(r1)
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)
print("*******************")
r2 = Rectangle(100, 200)
print(r2 > r1)
print("*******************")
print(r1._width)
r1._width = -100
print(r1._width)
print("*******************")
print(r1.get_width())
print(r1.set_width(2))
print("*******************")
