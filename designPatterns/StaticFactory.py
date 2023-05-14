class StaticFactory:
    __nome = None

    def __init__(self, nome):
        self.__nome = nome

    def factory(nome):
        return StaticFactory(nome);

    def getNome(self):
        return self.__nome