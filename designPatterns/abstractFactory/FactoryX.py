from AbstractFactory import AbstractFactory
from CustomProduct import CustomProduct
from ProductAX import ProductAX
from ProductBX import ProductBX

class FactoryX(AbstractFactory):

    @staticmethod
    def createProductA(name) -> CustomProduct:
        return ProductAX(name)

    @staticmethod
    def createProductB(name) -> CustomProduct:
        return ProductBX(name)


