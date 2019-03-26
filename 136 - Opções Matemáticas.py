#136 - Opções Matemáticas

repetir = 'S'
while repetir == 'S':
    nome = input('Seu Nome: ')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite Outro Número: '))
    op = int(input('Digite a Operação - 1.Add, 2.Subt, 3.Multi, 4.Div, 5.Sair: '))
    if op == 1:
        res = n1 + n2
        print(f'Resultado da Soma: {n1} + {n2} = {res}')
    elif op == 2:
        res = n1 - n2
        print(f'Resultado da Subtração: {n1} - {n2} = {res}')
    elif op == 3:
        res = n1*n2
        print(f'Resultado da Multiplicação: {n1} x {n2} = {res}')
    elif op == 4:
        res = n1/n2
        print(f'Resultado da Divisão: {n1}/{n2} = {res}')
    elif op == 5:
        print('Você saiu do programa.')
    else:
        print('Entrada Inválida.')

    print()
    print(f'Deseja Repetir a Operação, Sr(a). {nome}? - S ou N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado. Obrigado(a)!')
        break
else:
    print('Opção Inválida!')