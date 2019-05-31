#006 - Teste 006

from Ex006 import *

def Menu():
    while True:
        print('Bem-Vindo(a) ao Terminal de Recarga do VEM')
        print('Menu Principal\n1-Recarregar VEM Estudante\n2-Recarregar VEM Trabalhador\n3-Sair')
        print()
        r = input('Opção: ')
        if r == '1':
            idCard = input('Identificador do Seu Cartão: ')
            nome = input('Digite o seu nome: ')
            cpf = input('Seu CPF: ')
            IE = input('Instituição de Ensino na qual você estuda: ')
            Cliente = VemEstudante(idCard, nome, cpf, IE)
            print('Quer adicionar saldo? S/N')
            R = input('Resposta: ').upper()
            if R == 'S':
                S = input('Adicione seu saldo: ')
                S = int(S)
                print(Cliente.addSaldo(S))
                print()
                print(Cliente.VerificarSaldo())
                print()
                passagem = 3.45
                Cliente.pagar(passagem)
                print()
                print(Cliente.VerificarSaldo())
                print()
            elif R == 'N':
                print('Obrigado(a) e volte sempre.')
        elif r == '2':
            idCard = input('Identificador do seu cartão: ')
            nome = input('Seu Nome: ')
            cpf = input('Seu CPF: ')
            empresa = input('Empresa em que você trabalha: ')
            Trab = VemTrabalhador(idCard, nome, cpf, empresa)
            print('Quer adicionar saldo? S/N')
            R = input('Resposta: ').upper()
            if R == 'S':
                S = input('Adicione o seu saldo: ')
                S = int(S)
                print(Trab.addSaldo(S))
                print()
                print(Trab.VerificarSaldo())
                print()
                passagem = 3.45
                Trab.debitar(passagem)
                print()
                print(Trab.VerificarSaldo())
                print()
            elif R == 'N':
                print('Obrigado(a) e volte sempre.')
        elif r == '3':
            print('Volte sempre!')
            break

Menu()