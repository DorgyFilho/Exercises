#013 - Jogo de Dados

from random import randint

j1 = 'Dorgival'
j2 = 'Himari'
j3 = 'Cecilia'
p1 = 0
p2 = 0
p3 = 0
rj1 = 0
rj2 = 0
rj3 = 0
maisRapido = 0
maisEficiente = ''
vencedor = ''

while True:
    p1 += randint(1,6)
    rj1 += 1
    p2 += randint(1,6)
    rj2 += 1
    p3 += randint(1,6)
    rj3 += 1

    if rj1 > maisRapido and p1 >= 18:
        maisRapido = rj1
        p1 = 18
        maisEficiente = j1
        vencedor = maisEficiente
        print(f'O(a) vencedor(a) é {vencedor}')
        break
    if rj2 > maisRapido and p2 >= 18:
        maisRapido = rj2
        p2 = 18
        maisEficiente = j2
        vencedor = maisEficiente
        print(f'O(a) vencedor(a) é {vencedor}')
        break
    if rj3 > maisRapido and p3 >= 18:
        maisRapido = rj3
        p3 = 18
        maisEficiente = j3
        vencedor = maisEficiente
        print(f'O(a) vencedor(a) é {vencedor}')
        break

print('Jogo Encerrado!')