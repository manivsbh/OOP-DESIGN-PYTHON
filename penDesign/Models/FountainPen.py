from abc import ABC
from Models.Color import Color
from Pen import Pen
from PenType import PenType


class FountainPen(Pen, ABC):

    def __init__(self, price, company, name, pen_type, write_behaviour):
        super().__init__(price, company, name, PenType.FOUNTAIN, write_behaviour)

    def get_color(self) -> Color:
        pass

    def write(self):
        pass
