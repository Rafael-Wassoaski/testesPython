from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def operacao(self, valorA: float, valorB: float):
        pass