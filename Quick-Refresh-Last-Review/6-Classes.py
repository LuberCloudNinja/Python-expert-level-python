class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        print(height / width)

    @property
    def width(self):
        return self._width

    @width.setter

    @property
    def height(self):
        return self._height

    @height.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive!")
        else:
            self.width = width
    # def perimeter(self):
    #     return 2 * (self.self_width + self._height)

    # def get_width(self):
    #     return self._width
    #
    # def set_width(self, width):
    #     if width <= 0:
    #         raise ValueError('Width must be positive')
    #     else:
    #         self._width = width

    def __str__(self):
        return f'Rectangle: width={self.width} height={self.height}'

    def __repr__(self):
        return f'Rectangle: {self.width} {self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    # def __lt__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.area() < other.area()
    #     else:
    #         return NotImplemented


r1 = Rectangle(10, 20)
r1.width = 200
print(r1.width)
