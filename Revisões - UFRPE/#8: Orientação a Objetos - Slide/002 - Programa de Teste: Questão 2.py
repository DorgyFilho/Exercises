#002 - Teste da Questão 002

from Ex002 import *

nome = input('Seu Nome: ')
sal = float(input('Salário: '))
taxaInc = float(input('Taxa de aumento: '))
Novo = Funcionario(nome, sal, taxaInc)
print('Nome: %s\nSalário Atual: R$%.2f\nNovo Salário: R$%.2f' %(Novo.NomeFunc(), Novo.atualSalario(), Novo.aumento()))