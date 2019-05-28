#005 - Programa de Teste: Questão 005

from Ex005 import *

MeuComb = int(input('Consumo do Carro Por Litro, em Km: '))
MeuCarro = Carro(MeuComb)
print(MeuCarro.getGas())
print()
Add = int(input('Quantidade de combustível a ser adicionada: '))
MeuCarro.addGas(Add)
print(MeuCarro.getGas())
print()
Dist = int(input('Distância Percorrida: '))
print(MeuCarro.andar(Dist))
print(MeuCarro.getGas())
print()
NovaDist = int(input('Nova Distância: '))
print(MeuCarro.andar(NovaDist))
print(MeuCarro.getGas())