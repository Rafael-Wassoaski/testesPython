class Singleton:
    __Singleton = None
    __nome = None

    def __init__(self, nome):
        self.__nome = nome

    @staticmethod
    def getInstance(nome):
        if Singleton.__Singleton == None:
            Singleton.__Singleton = Singleton(nome)

        return Singleton.__Singleton

    def getNome(self):
        return self.__nome