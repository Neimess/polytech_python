from abc import ABC, abstractmethod
from numbers import Number
from math import sqrt, sin, radians, pi


class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        """
        Abstract method for initializing a shape.
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        Abstract method for calculating the area of a shape.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Abstract method for returning the string representation of a shape.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method for returning the formal string representation of a shape.
        """
        pass


class Triangle(Shape):

    def __init__(self, a: Number, b: Number, c: Number):
        """
        Initializes a triangle with the given side lengths.

        Args:
        a (Number): The length of side a.
        b (Number): The length of side b.
        c (Number): The length of side c.

        Raises:
        TypeError: If one sides are not numeric.
        ValueError: If any side is less than 0 or if
        the sides do not form a valid triangle.
        """
        if not (isinstance(a, Number)
                and not isinstance(b, Number)
                and not isinstance(c, Number)):
            raise TypeError("All sides should be numeric")
        if a < 0 or b < 0 or c < 0:
            raise ValueError('Sides can\'t be less 0')
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError('Triangle with this sides can\'t exist')
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self) -> Number:
        """
        Property for retrieving the length of side a.
        """
        return self._a

    @property
    def b(self) -> Number:
        """
        Property for retrieving the length of side b.
        """
        return self._b

    @property
    def c(self) -> Number:
        """
        Property for retrieving the length of side c.
        """
        return self._c

    @abstractmethod
    def area(self) -> Number:
        """
        Abstract method for calculating the area of a triangle.
        """
        pass

    def perimeter(self) -> Number:
        """
        Calculates the perimeter of the triangle.
        """
        return (self._a + self._b + self._c)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with area = {self.area()}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, a={self._a}, b={self._b}, c={self._c})"


class RightTriangle(Triangle):

    def __init__(self, side: Number):
        """
        Initializes a right-angled triangle with the given side length
        and have a new paramether angle.

        Args:
        a (Number): The length of side a.
        b (Number): The length of side b.
        c (Number): The length of side c.
        """
        super().__init__(side, side, side)
        self._angle = radians(60/pi)

    def area(self) -> Number:
        """
        Calculates the area of the right-angled triangle.
        """
        return (self._a * self._b * sin(self._angle) / 2)


class IsoscelesTriangle(Triangle):

    def __init__(self, a: Number, b: Number, c: Number, height: Number):

        super().__init__(a, b, c)

        if not isinstance(height, Number):
            raise TypeError("Hight should be numeric")
        if height < 0:
            raise ValueError('Hight can\'t be less 0')
        self._h = height

    def area(self) -> Number:
        return self._a * self._b * sin(self._h)


class Rectangle(Shape):

    def __init__(self, width: Number, height: Number):
        if not isinstance(width, Number) or not isinstance(height, Number):
            raise TypeError("Width and height should be numeric values")
        if width < 0 or height < 0:
            raise ValueError('Sides can\'t be less 0')
        self._width = width
        self._height = height

    @property
    def width(self) -> Number:
        return self._width

    @property
    def height(self) -> Number:
        return self._height

    def area(self) -> Number:
        return self._height * self._width

    def diagonal(self) -> Number:
        return sqrt(self._width ** 2 + self._height ** 2)

    def perimeter(self) -> Number:
        return self._height * 2 + self._width * 2

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with area = {self.area()}."

    def __repr__(self) -> str:
        return f"{self._type}, width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side: Number):
        return super().__init__(side, side)

    def __repr__(self) -> str:
        return f"{self._type}, side={self.width})"
