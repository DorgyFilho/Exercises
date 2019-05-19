#006 - Matriz Dicionários

M = {}

lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    aux = []
    for c in range(1, col+1):
        elem = int(input(f'Posição {l},{c}: '))
        aux.append(str(elem))
    M[(l,c)] = aux

listaMatriz = list(M.values())

for a in listaMatriz:
    for b in a:
        print(b, end=' ')
    print()