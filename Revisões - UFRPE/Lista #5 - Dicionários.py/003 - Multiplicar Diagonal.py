#003 - Multiplicar Diagonal

m = {}

L = int(input('Linha: '))
C = int(input('Coluna: '))

for l in range(1, L+1):
    aux = []
    for c in range(1, C+1):
        elem = int(input(f'Posição {l},{c}: '))
        aux.append(elem)
    m[(l,c)] = aux

M = list(m.values())

diagonal = [M[i][i] for i in range(len(M))]
print(diagonal)
print()

totalDiag = 1
for i in diagonal:
    totalDiag *= i
print(f'Resultado: {totalDiag}')
