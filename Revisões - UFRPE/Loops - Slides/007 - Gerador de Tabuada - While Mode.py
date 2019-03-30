#007 - Gerador de Tabuada: While Mode

repetir = 'S'
while repetir == 'S':
    num = int(input('Número a ser multiplicado: '))
    multi = 1
    result = 0
    while multi <= 10:
        result = num * multi
        print(f'{num} x {multi} = {result}')
        multi += 1
    print()
    print('Deseja repetir a operação? - S/N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida!')