from Singleton import Singleton
from StaticFactory import StaticFactory
from Builder import BuilderPattern



singleton = Singleton.getInstance("teste static")

print(singleton.getNome())


staticFactory = StaticFactory.factory("teste factory")
staticFactory2 = StaticFactory.factory("teste factory2")


print(staticFactory.getNome())
print(staticFactory2.getNome())
print(staticFactory.getNome())

builder = BuilderPattern.create().comNome("rafa").comIdade(24).comCargo("Dev senior").construct();

print(builder)



