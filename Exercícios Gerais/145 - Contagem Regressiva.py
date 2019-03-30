#145 - Contagem Regressiva

from time import sleep

tempo = 11
while tempo > 0:
    tempo -= 1
    sleep(1)
    print(tempo)
    if tempo == 0:
        sleep(1)
        print('Boom!')