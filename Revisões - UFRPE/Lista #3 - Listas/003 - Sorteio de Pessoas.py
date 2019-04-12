#003 - Sorteio de Pessoas

import random
import time

Nomes = ['Dorgival', 'Himari', 'Cecília', 'Rebeca', 'Saulo', 'Sharon', 'Charlotte', 'Jonathas', 'Juliana', 'Valentina']
Sorteados = []

random.shuffle(Nomes)

for i in range(len(Nomes)):
    if len(Nomes) > 0:
        random.shuffle(Nomes)
        sorteado = Nomes.pop(0)
        Sorteados.append(sorteado)
    if Nomes == ' ':
        break
    print()
    time.sleep(2)
    print(f'Sorteado(a): {sorteado}')
    time.sleep(2)
    for k in range(len(Nomes)):
        print(Nomes[k])
    print(Sorteados)

