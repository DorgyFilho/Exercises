#Arquivo da Questão 6

from Nomes import *

lNome = ['alucard', 'richter', 'dracula', 'anette', 'shanoa', 
        'amarilys', 'akiza', 'aromage', 'anzu']

verListas = lerLista(lNome)
print(verListas)

print()

Filtro = CoMa(lNome)
print(Filtro)

print()

resultado = imprimir(Filtro)
for i in resultado:
    print(i)