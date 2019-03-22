#086 - Crescimento Populacional - Modo Interativo


repetir = 'S'
while repetir == 'S':
    paisA = int(input('População A: '))
    paisB = int(input('População B: '))
    taxaA = float(input('Taxa País A: '))
    taxaB = float(input('Taxa País B: '))
    tA = (taxaA/100)
    tB = (taxaB/100)

    anos = 0

    while paisA < paisB:
        paisA *= (1+tA)
        paisB *= (1+tB)
        anos += 1

    print(f'País A: {paisA:.0f}\nPaís B: {paisB:.0f}\nQtd. Anos: {anos}')

    print()

    print('Deseja repetir a operação? - S ou N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida.')
