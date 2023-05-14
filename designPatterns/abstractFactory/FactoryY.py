from AbstractFactory import AbstractFactory
from CustomProduct import CustomProduct
from ProductAY import ProductAY
from ProductBY import ProductBY

class FactoryY(AbstractFactory):
    @staticmethod
    def createProductA(name) -> CustomProduct:
        return ProductAY(name)

    @staticmethod
    def createProductB(name) -> CustomProduct:
        return ProductBY(name)