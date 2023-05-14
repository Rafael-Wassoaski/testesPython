from FactoryX import FactoryX
from FactoryY import FactoryY

ax = FactoryX.createProductA("nome1");
bx = FactoryX.createProductB("nome2");
ay = FactoryY.createProductA("nome3");
by = FactoryY.createProductB("nome4");


print(ax.getNome())
print(bx.getNome())
print(ay.getNome())
print(by.getNome())