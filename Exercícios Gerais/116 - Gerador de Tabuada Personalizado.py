#116 - Gerador de Tabuada Personalizado

repetir = 'S'
while repetir == 'S':
    num = int(input('Número a ser multiplicado: '))
    inicio = int(input('Multiplicador Inicial: '))
    fim = int(input('Multiplicador Final: '))
    if inicio > fim:
        print('Digite um valor superior referente ao fim.')
        continue
    else:
        for i in range(inicio, fim+1):
            res = num*i
            print(f'{num} x {i} = {res}')
    print()
    print('Deseja repetir a operação? - S ou N')
    print()
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Inválido!')
