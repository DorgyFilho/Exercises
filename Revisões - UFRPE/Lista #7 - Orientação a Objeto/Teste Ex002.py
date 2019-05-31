#002 - Teste do Programa 002

from Ex002 import *

def Menu():
    while True:
        print('1-Cadastrar\n2-Sair')
        print()
        op = input('Resposta: ')
        if op == '1':
            nome = input('Seu nome: ')
            sal = input('Seu Salário: ')
            sal = float(sal)
            F = Func(nome, sal)
            F.pegaNome()
            F.pegaSalario()
            print()
            print(F)
        elif op == '2':
            print('Cadastro Encerrado.')
            break

Menu()