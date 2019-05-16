#008 - Matriz

Matriz = []

lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        pos = int(input(f'Posição {l},{c}: '))
        linha.append(pos)
    Matriz.append(linha)

for a in Matriz:
    for b in a:
        print(b, end=' ')
    print()