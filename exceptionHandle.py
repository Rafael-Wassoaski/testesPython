


try:
    lista = [];

    valor1: float = float(input("Digite um valor "))
    valor2: float = float(input("Digite outro valor "))

    lista.append(valor1)
    lista.append(valor2)
    divisao = lista[0] / lista[1];
except ValueError:
    print("Voce digitou um caracter no lugar de um numero")
except IndexError:
    print("O index usado no vetor que armazena os valores está fora do range de 2")
except ZeroDivisionError:
    print("Você digitou o divisor como sendo 0")
except KeyboardInterrupt:
    print("Usuario encerrando o programa")
else:
    print(f"valor final da divisao {divisao}")

