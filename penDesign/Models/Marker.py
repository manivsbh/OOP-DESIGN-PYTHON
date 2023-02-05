from abc import ABC
from Models.Color import Color
from Pen import Pen
from PenType import PenType
from RefilInterface import RefilInterface


class Marker(Pen, ABC, RefilInterface):

    def __init__(self, price, company, name, pen_type, write_behaviour):
        super().__init__(price, company, name, PenType.MARKER, write_behaviour)

    def get_color(self) -> Color:
        pass

    def write(self):
        pass

    def get_refil(self):
        return None

    def can_change_refil(self):
        pass

    def change_refil(self, new_refil: Refil):
        pass
