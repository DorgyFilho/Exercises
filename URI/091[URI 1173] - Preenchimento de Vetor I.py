#091 - Preenchimento de Vetor I

n = []

v = int(input())
n.append(v)

for i in range(10):
    v *= 2
    n.append(v)

for i in range(10):
    print('N[{}] = {}'.format(i, n[i]))

