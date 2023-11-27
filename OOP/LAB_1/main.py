from abc import ABC
from numbers import Number


class Animal(ABC):
    def __init__(self, name: str, type_: str, age: int):
        """
        Initial of class
        :param name: Name of animal
        :param type: Type of animal
        :param age: Age of animal
        Examples:
        >>> animal = Animal('Potty', 'Cat', 5)
        """
        if not isinstance(name, str):
            raise TypeError("Name of animal should be a str type")
        if not isinstance(type_, str):
            raise TypeError("Type of animal should be a str type")
        if not isinstance(age, int):
            raise TypeError("Age of animal must be a int type")

    def eat(self, food: str) -> str:
        """
        Eat food and return a message.

        Args:
        food (str): The food to eat.

        Returns:
        str: A message about eating the food.

        :return: f'{self.name} eats the {food} and feels satisfied'

        Examples:
        >>> being = Animal("Bob", "Dog", 3)
        >>> being.eat("apple")
        """
        if not isinstance(food, str):
            raise TypeError("Food of animal should be a str type")

    def reproduce(self) -> str:
        """
        Reproduce and return a message.

        Returns:
            str: A message about the reproduction.

        :return: f'{self.name} participates in the process of reproduction'

        Examples:
        >>> being = Animal("Alice", "Cat", 2)
        >>> being.reproduce()
        """

    def whats_age(self) -> int:
        """
        Return age

        Returns:
             int: A message about the age of animal.

        Examples:
        >>> being = Animal("Alice", "Parrot", 30)
        >>> being.reproduce()
        """


class Rectangle(ABC):
    def __init__(self, width: Number, height: Number):
        """
            Initializion of class Rectangle
            :param width: width of shape
            :param height: height of shape

            Setting attributes:
            self._width = width
            self._height = height
            Setting additional attributes:
            for key, value in kwargs.iteritems():
            setattr(self, key, value)
            Examples:
            >>> shape = Rectangle(3,5)
        """
        if not isinstance(width, Number) or not isinstance(height, Number):
            raise TypeError("Width and height should be numeric values")
        if width < 0 or height < 0:
            raise ValueError('Sides can\'t be less 0')

    def area(self) -> Number:
        """Return area of shape


           Returns:
           Number: self.height * self.width

           Examples:
           >>> shape = Rectangle(3,5)
           >>> shape.area()
        """


class Vehicle(ABC):
    def __init__(self,
                 brand: str,
                 model: str,
                 **kwargs):
        """
            Initial of class
            :param age: Age of animal
            :param max_speed: Name of animal
            :param **kwargs: Additional paramethers

            Setting additional attributes:
            for key, value in kwargs.iteritems():
            setattr(self, key, value)
            Examples:
            >>> tesla = Vehicle('Testa', 'Model X', max_speed=300.00)
        """
        if not isinstance(brand, str):
            raise TypeError("Brand of vehicle should be a str type")
        if not isinstance(model, str):
            raise TypeError("Model of vehicle should be a str type")
        if kwargs.get('max_speed') and not isinstance(
                                    kwargs.get('max_speed'), Number):
            raise TypeError("Max_speed must be a number type")
        if kwargs.get('max_speed') and kwargs.get('max_speed') < 0:
            raise ValueError("Speed can't be less 0")

    def start_engine(self) -> str:
        """Start the vehicle's engine and return a message.

        Returns:
        str: A message about starting the engine.

        Examples:
        >>> car = Vehicle("Ford", "Focus")
        >>> car.start_engine()
        """
        ...

    def drive(self, destination: str, avg_speed: float) -> str:
        """Drive the vehicle to a destination at a certain
        speed and return a message.

        Args:
        destination (str): The destination to drive to.
        avg_speed (float): The speed of driving.

        Returns:
        str: A message about driving to the destination at a certain speed.

        Examples:
        >>> car = Vehicle("Tesla", "Model S", max_speed=250)
        >>> car.drive("New York", 100)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
