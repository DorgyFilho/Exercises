#093 - Troca Em Vetor

N = []

for i in range(20):
    Y = int(input(''))
    N.append(Y)

N.reverse()

for i in range(20):
    print('N[%d] = %d' %(i, N[i]))

