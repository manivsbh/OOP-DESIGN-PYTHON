from abc import ABC, abstractmethod
from Refil import Refil


class RefilInterface(ABC):
    @abstractmethod
    def get_refil(self):
        pass

    @abstractmethod
    def can_change_refil(self):
        pass

    @abstractmethod
    def change_refil(self, new_refil: Refil):
        pass
