#009 - Teste Exercício 009

from Ex009 import *

# comum = input('Nome Comum: ')
# latim = input('Nome em latim: ')   
comum = 'Papagaio-Verdadeiro'
latim = 'Amazona aestiva'
Lista = latim.split()
Resultado = Animal('Papagaio-Verdadeiro', 'Amazona aestiva')
print(Resultado.validoLatim(latim))
print(Resultado.Genero(Lista[0]))
print(Resultado.Especie(Lista[1]))