#003 - Fatorial: Modo Simples/Modo Sofisticado

#repetir = 'S'
#while repetir == 'S':
#    fat = 1
#    num = int(input('Digite um Número: '))
#    if num > 20:
#        print('Apenas um número menor ou igual a 20 pode ser digitado.')
#        continue
#    else:
#        valor = num
#        while valor > 0:
#            fat *= valor
#            valor -= 1
#        print(f'O fatorial de {num} é {fat}')
#    
#    print()
#    print('Deseja repetir a operação? - S/N')
#    repetir = input('Resposta: ').upper()
#    if repetir == 'N':
#        print('Programa Encerrado.')
#        break
#else:
#    print('Opção Inválida!')

#Modo Sofisticado
repetir = 'S'
while repetir == 'S':
    fat = 1
    num = int(input('Número: '))
    if num > 20:
        print('Digite um número menor ou igual a 20!')
        continue
    else:
        valor = num
        print()
        print(f'Fatorial de {num}! = ',end=' ')
        while valor > 0:
            print(f'{valor}', end=' ')
            print('.' if valor > 1 else '=', end=' ')
            fat *= valor
            valor -= 1
        print(f'{fat}')
    
    print()
    print('Deseja repetir a operação? - S/N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida!')