class BuilderPattern:
    __nome: str = None
    __idade: int = 0
    __cargo: str = None

    def __init__(self, nome, idade, cargo):
        self.__nome = nome
        self.__idade = idade
        self.__cargo = cargo

    class Builder:
        __nome: str = None
        __idade: int = 0
        __cargo: str = None

        def comNome(self, nome: str):
            self.__nome = nome
            return self

        def comIdade(self, idade: int):
            self.__idade = idade
            return self

        def comCargo(self, cargo: str):
            self.__cargo = cargo
            return self


        def construct(self):
            return BuilderPattern(self.__nome, self.__idade, self.__cargo)

    @staticmethod
    def create():
        return BuilderPattern.Builder()

    def __str__(self) -> str:
        return self.__nome + " " + str(self.__idade) + " " + self.__cargo + " "


