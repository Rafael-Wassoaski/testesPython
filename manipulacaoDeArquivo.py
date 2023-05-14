import re

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open("./alunos.txt", "w") as alunosTxt:
    for chave, valor in alunos.items():
        alunosTxt.write(f"{chave},{valor}\n")



with open("./alunos.txt") as text:
    for txt in text:
        print(txt)


frase = "Opa como vai, meu numero eh (47)00010-0000"
resultado = re.search("\(\d{2}\)\d{4,5}-\d{4}", frase)
print(resultado)

frase = "Placa do carro ABC-5677"
resultado = re.search("[A-Z]{3}-\d{4}", frase)
print(resultado)

frase = "meu email eh teste@teste.com"
resultado = re.search("\w+@\w+\.\w+", frase)
print(resultado)


frase = "teste@teste.com meu email eh teste@teste.com"
resultado = re.match("\w+@\w+\.\w+", frase)
print(resultado)

frase = "teste@teste.com meu email eh teste@teste.com"
resultado = re.findall("\w+@\w+\.\w+", frase)
print(resultado)


numeros = "123456789 teste 123424"
resultadoNum = re.findall("\d+", numeros)
print(resultadoNum)

cep = "89464-100 teste 123424"
resultadoCep = re.findall("\d{5}-\d{3}", cep)
print(resultadoCep)

url = "89464-100 teste 123424 http://www.udemy.com/course/machine-learning-e-data-science-com-python-y/learn/lecture/26214424#overview"
resultadoUrl = re.findall("https?://.*", url)
print(resultadoUrl)
