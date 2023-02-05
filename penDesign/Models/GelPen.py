from abc import ABC, abstractmethod
from Models.Color import Color
from PenType import PenType
from Pen import Pen
from RefilInterface import RefilInterface
from Refil import Refil


class GelPen(Pen, ABC, RefilInterface):

    def __init__(self, price, company, name, pen_type, write_behaviour):
        super().__init__(price, company, name, PenType.GEL, write_behaviour)

    class Builder:
        refil: Refil
        can_change_refil: bool = False

        @staticmethod
        def set_refil(self):
            return self.refil



    def get_color(self) -> Color:
        pass

    def write(self):
        pass

    def get_refil(self):
        pass

    def can_change_refil(self):
        pass

    def change_refil(self, new_refil: Refil):
        pass
