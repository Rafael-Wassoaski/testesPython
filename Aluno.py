class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota2 + self.nota1) / 2

    def dados(self):
        return f"nome: {self.nome}\n nota 1: {self.nota1}\n nota 2: {self.nota2}"

    def resultado(self):
        if self.media() >= 6:
            return "aprovado"
        return "reprovado"


aluno1 = Aluno("rafa", 10, 10)
aluno2 = Aluno("rafa2", 10, 10)

print(aluno1.dados())
print(aluno2.dados())

print(aluno1.media())
print(aluno2.media())

print(aluno1.resultado())
print(aluno2.resultado())