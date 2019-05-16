#010 - Pedra, Papel e Tesoura

jogador1 = 0
jogador2 = 0
#Round 1
j1 = input('Digite Pedra, Papel ou Tesoura: ').lower()
j2 = input('Digite Pedra, Papel ou Tesoura: ').lower()

if j1 == 'pedra' and j2 == 'tesoura':
    jogador1 += 1
elif j1 == 'papel' and j2 == 'pedra':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'papel':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'pedra':
    jogador2 += 1
elif j1 == 'pedra' and j2 == 'papel':
    jogador2 += 1
elif j1 == 'papel' and j2 == 'tesoura':
    jogador2 += 1 
elif j1 == j2:
    print('Empate!')
else:
    print('Inválido!')

#Round 2
j1 = input('Digite Pedra, Papel ou Tesoura: ').lower()
j2 = input('Digite Pedra, Papel ou Tesoura: ').lower()

if j1 == 'pedra' and j2 == 'tesoura':
    jogador1 += 1
elif j1 == 'papel' and j2 == 'pedra':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'papel':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'pedra':
    jogador2 += 1
elif j1 == 'pedra' and j2 == 'papel':
    jogador2 += 1
elif j1 == 'papel' and j2 == 'tesoura':
    jogador2 += 1 
elif j1 == j2:
    print('Empate!')
else:
    print('Inválido!')

#Round 3
j1 = input('Digite Pedra, Papel ou Tesoura: ').lower()
j2 = input('Digite Pedra, Papel ou Tesoura: ').lower()

if j1 == 'pedra' and j2 == 'tesoura':
    jogador1 += 1
elif j1 == 'papel' and j2 == 'pedra':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'papel':
    jogador1 += 1
elif j1 == 'tesoura' and j2 == 'pedra':
    jogador2 += 1
elif j1 == 'pedra' and j2 == 'papel':
    jogador2 += 1
elif j1 == 'papel' and j2 == 'tesoura':
    jogador2 += 1 
elif j1 == j2:
    print('Empate!')
else:
    print('Inválido!')

if jogador1 > jogador2:
    print('Jogador 2 lava a louça!')
if jogador1 < jogador2:
    print('Jogador 1 lava a louça!')
if jogador1 == 3 and jogador2 == 0:
    print('Jogador 2 lavará a louça do jantar!')
if jogador1 == 0 and jogador2 == 3:
    print('Jogador 1 lavará a louça do jantar!')
if jogador1 == jogador2:
    print('Ambos lavam a louça!')