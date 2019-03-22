#068 - Pedra, Papel e Tesoura

opcao = ['PEDRA', 'PAPEL', 'TESOURA']

scrJ1 = 0
scrJ2 = 0
tentativas = 4
while tentativas > 0:
    j1 = input('Escolha a sua opção - Pedra, Papel ou Tesoura: ').upper()
    j2 = input('Escolha a sua opção - Pedra, Papel ou Tesoura: ').upper()
    if j1 == j2:
        print('Empate!!')
        tentativas -= 1
    elif j1 == 'PEDRA' and j2 == 'TESOURA':
        print('Pedra quebra tesoura! Jogador 1 Vence.')
        scrJ1 += 1
        tentativas -= 1
    elif j1 == 'PAPEL' and j2 == 'PEDRA':
        print('Papel embrulha pedra! Jogador 1 Vence.')
        scrJ1 += 1
        tentativas -= 1
    elif j1 == 'TESOURA' and j2 == 'PAPEL':
        print('Tesoura corta papel! Jogador 1 Vence.')
        scrJ1 += 1
        tentativas -= 1
    elif j1 == 'TESOURA' and j2 == 'PEDRA':
        print('Pedra quebra tesoura! Jogador 2 Vence.')
        scrJ2 += 1
        tentativas -= 1
    elif j1 == 'PEDRA' and j2 == 'PAPEL':
        print('Papel embrulha pedra! Jogador 2 Vence.')
        scrJ2 += 1
        tentativas -= 1
    elif j1 == 'PAPEL' and j2 == 'TESOURA':
        print('Tesoura corta papel! Jogador 2 Vence.')
        scrJ2 += 1
        tentativas -= 1
    else:
        print('Movimento inválido!')

    if scrJ1 == 3 and tentativas == 0:
        print('Jogador 2 lavará a louça!')
        break
    elif scrJ2 == 3 and tentativas == 0:
        print('Jogador 1 lavará a louça!')
        break
    elif scrJ2 == scrJ1 and tentativas == 0:
        print('Ambos lavarão a louça')
        break
    