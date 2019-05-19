#005 - Multiplicar Ímpares da Matriz

m = {}

lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        elem = int(input(f'Posição {l},{c}: '))
        linha.append(str(elem*2 if elem % 2 != 0 else elem))
    m[(l,c)] = linha

listaMatriz = list(m.values())

for i in listaMatriz:
    for j in i:
        print(j, end=' ')
    print()