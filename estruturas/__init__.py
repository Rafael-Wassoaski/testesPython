import numpy as np;

def createList():
    lista: list = [];
    total = 0

    for index in range(0, 5):
        valor:  int = int(input("Digite um valor: "))
        lista.append(valor)

    for index in range(len(lista)):
        print(lista[index])
        total += lista[index]

        print(f"total {total}")

def createDictionary():
    dicionario = {}
    total: float = 0

    for index in range(0, 3):
        nome: str = str(input("Digite o nome do aluno: "))
        nota: float = float(input(f"Digite a nota do aluno {nome}: "))
        dicionario[nome] = nota

    # for key in dicionario.keys():
    #     total += dicionario[key]

    for value in dicionario.values():
        total += value

    print(f"soma total das notas {total}")
    print(f"media {total/3}")



def iterateArray():
    matrix = np.array([
        [3, 4, 1],
        [3, 1, 5]
    ])

    total: int =0

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i][j])

            total += matrix[i][j]

    print(f"total {total}")





# createList();
# createDictionary()
# iterateArray()
