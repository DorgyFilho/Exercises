#004 - Mega-Sena

from random import randint

dez = [0,1,2,3,4,5,6,7,8,9]
uni = [0,1,2,3,4,5,6,7,8,9]

sorteados = []

for i in range(6):
    d = randint(0,9)
    u = randint(0,9)
    if not (d == 0 and u == 0) and not (d in sorteados and u in sorteados):
        sorteados.append(d*10+u)

for num in sorteados:
    print(num, end=' ')

