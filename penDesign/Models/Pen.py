from abc import ABC, abstractmethod
from Models.PenType import PenType
from Models.Color import Color


class Pen(ABC):
    __price: int
    __company: str
    __pen_type: PenType
    __name: str

    def __init__(self, price, company, name, pen_type, write_behaviour):
        self.write_behaviour = write_behaviour
        self.__price = price
        self.__company = company
        self.__name = name
        self.__pen_type = pen_type

    # def write(self):
    #     self.write_behaviour.write()

    @abstractmethod
    def get_color(self) -> Color:
        pass

    @abstractmethod
    def write(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def pen_type(self):
        return self.pen_type

    @pen_type.setter
    def pen_type(self, pen_type):
        self.pen_type = pen_type
