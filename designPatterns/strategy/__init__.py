from Divisao import Divisao
from Subtracao import Subtracao
from Multiplicao import Multiplicao
from Adicao import Adicao
from Operacao import Operacao

operacao: Operacao = Adicao();

print(operacao.operacao(2,2))

operacao: Operacao = Divisao();

print(operacao.operacao(2,2))

operacao: Operacao = Subtracao();

print(operacao.operacao(2,2))

operacao: Operacao = Multiplicao();

print(operacao.operacao(2,2))