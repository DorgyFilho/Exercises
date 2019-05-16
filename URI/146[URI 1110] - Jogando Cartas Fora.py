#146 - Jogando Cartas Fora

while True:

    N = int(input())

    if N == 0:
        break

    Stardust = []
    for k in range(1, N+1):
        Stardust.append(k)

    BlackRose = []
    while len(Stardust) > 1:
        BlackRose.append(Stardust.pop(0))
        Stardust.insert(len(Stardust)-1, Stardust.pop(0))

    print('Discarded cards: %s' %str(BlackRose).replace('[','').replace(']',''))
    print('Remaining card: %s' %str(Stardust[0]))
