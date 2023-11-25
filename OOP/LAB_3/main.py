from abc import ABC, abstractmethod


class Book(ABC):
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}"

    @abstractmethod
    def __repr__(self) -> str:
        pass


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages
        if not isinstance(pages, int):
            raise TypeError("Pages of Audiobook could be int ")
        if pages < 0:
            raise ValueError("Pages of paperbook could't be less then zero")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Pages of PaperBook should be an int")
        if value < 0:
            raise ValueError("Pages of PaperBook couldn't be less than zero")
        self._pages = value

    def __str__(self):
        return super().__str__() + f'. Количество страниц {self._pages}'

    def __repr__(self) -> str:
        return (
            f"PaperBook(name={self._name!r}, author={self._author!r},"
            f"pages={self._pages})"
        )


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Duration of Audiobook could be float")
        if duration < 0:
            raise ValueError("Duration of audiobook could't be less then zero")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Duration of AudioBook should be a number")
        if value < 0:
            raise ValueError(
                "Duration of AudioBook couldn't be less than zero")
        self._duration = value

    def __str__(self) -> str:
        return super().__str__() + f'. Длительность: {self.duration}'

    def __repr__(self) -> str:
        return (
            f"AudioBook(name={self.name!r}, author={self.author!r}, "
            f"duration={self.duration})"
        )
