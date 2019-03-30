#099 - Fatorial Limitado

repetir = 'S'
while repetir == 'S':
    num = int(input('Número para achar o fatorial: '))
    fat = 1
    if num >= 1 and num < 16:
        for i in range(1, num+1):
            fat *= i
        print(f'O fatorial de {num} é {fat}')
    else:
        print('Número fora do intervalo.')
    print()
    print('Deseja repetir a operação? - S ou N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida!')
        
