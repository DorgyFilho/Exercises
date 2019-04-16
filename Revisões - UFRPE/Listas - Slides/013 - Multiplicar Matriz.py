M = []
L = int(input('L: '))
C = int(input('C: '))

for i in range(1, L+1):
  aux = []
  for j in range(1, C+1):
    V = int(input(f'{i}, {j}: '))
    aux.append(V)
  M.append(aux)

for a in M:
  for b in a:
    novaMatriz = 2*int(b)
    print(novaMatriz, end=' ')
  print()
  