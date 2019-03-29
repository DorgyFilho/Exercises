#151 - Jogo de Dados

from random import randint

p1 = 'dorgival'
p2 = 'cpu'
p3 = 'cpu2'
pj1 = 0
pj2 = 0
pj3 = 0
rj1 = 0
rj2 = 0
rj3 = 0
maisRapido = ''
maisEficiente = 0
vencedor = ''

while True:
    pj1 += randint(1,6)
    rj1 += 1
    pj2 += randint(1,6)
    rj2 += 1
    pj3 += randint(1,6)
    rj3 += 1

    if rj1 > maisEficiente and pj1 >= 18:
        maisEficiente = rj1
        pj1 = 18
        maisRapido = p1
        vencedor = maisRapido
        print(f'O vencedor é {vencedor}!')
        break
    if rj2 > maisEficiente and pj2 >= 18:
        maisEficiente = rj2
        pj2 = 18
        maisRapido = p2
        vencedor = maisRapido
        print(f'O vencedor é {vencedor}!')
        break
    if rj3 > maisEficiente and pj3 >= 18:
        maisEficiente = rj3
        pj3 = 18
        maisRapido = p3
        vencedor = maisRapido
        print(f'O vencedor é {vencedor}!')
        break

print()
print('Programa Encerrado!')





