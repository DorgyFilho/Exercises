#009 - Matriz

Matriz = []
lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    linha = []
    for c in range(1, col+1):
        valor = int(input('Valor: '))
        linha.append(valor)
    Matriz.append(linha)

for a in Matriz:
    for b in a:
        print(b, end=' ')
    print()