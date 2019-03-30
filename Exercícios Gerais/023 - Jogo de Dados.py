#023 - Jogo de Dados

from random import randint

jogador1 = 0
j1 = 0
jogador2 = 0
j2 = 0
jogador3 = 0
j3 = 0

while True:
    jogador1 += randint(1,6)
    j1 += 1
    jogador2 += randint(1,6)
    j2 += 1
    jogador3 += randint(1,6)
    j3 += 1
    if jogador1 == 18:
        if j1 < j2 and j1 < j3:
            print(f'Jogador A Conseguiu {jogador1} pontos em {j1} rodadas.')
            break
    elif jogador2 == 18:
        if j2 < j1 and j2 < j3:
            print(f'Jogador B conseguiu {jogador2} pontos em {j2} rodadas.')
            break
    elif jogador3 == 18:
        if j3 < j1 and j3 < j2:
            print(f'Jogador C conseguiu {jogador3} pontos em {j3} rodadas.')
            break
    else:
        if jogador1 > jogador2 and jogador1 > jogador3:
            print('O jogador A é o vencedor!')
            break 
        elif jogador2 > jogador1 and jogador2 > jogador3:
            print('O jogador B é o vencedor!')
            break
        elif jogador3 > jogador1 and jogador3 > jogador1:
            print('O jogador C é o vencedor!')
            break
        else:
            print('Empate!')
            break        

