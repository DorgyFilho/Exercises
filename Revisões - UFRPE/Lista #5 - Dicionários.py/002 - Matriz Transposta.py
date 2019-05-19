#002 - Matriz Transposta

m = {}

lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        elem = int(input(f'Pos {l}, {c}: '))
        linha.append(str(elem))
    m[(l,c)] = linha

    M = list(m.values())

    mTransp = [[M[c][l] for c in range(len(M))] for l in range(len(M[0]))]

for a in mTransp:
    for b in a:
        print(b, end=' ')
    print()
