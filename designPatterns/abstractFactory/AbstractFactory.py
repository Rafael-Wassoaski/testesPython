from CustomProduct import CustomProduct

class AbstractFactory:
    @staticmethod
    def createProductA(name) -> CustomProduct:
        pass
    @staticmethod
    def createProductB(name) -> CustomProduct:
        pass