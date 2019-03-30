#100 - Número Primo

repetir = 'S'
while repetir == 'S':
    num = int(input('Número: '))
    if (num % 2 != 0 or num == 2) and (num%3 != 0 or num == 3) and (num%5 != 0 or num == 5) and (num%7 != 0 or num == 7):
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')
    print()
    print('Deseja repetir a operação? - S ou N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida')
