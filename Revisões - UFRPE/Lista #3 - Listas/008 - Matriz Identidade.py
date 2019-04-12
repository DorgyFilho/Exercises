#008 - Matriz Identidade

Matriz = []
Ordem = int(input('Ordem da Matriz: '))

for i in range(Ordem):
    linha = []
    for j in range(Ordem):
        valor = int(input('Valor: '))
        if i == j:
            valor = 1
            linha.append(valor)
        else:
            valor = 0
            linha.append(valor)
    Matriz.append(linha)

for a in Matriz:
    for b in a:
        print(b, end=' ')
    print()