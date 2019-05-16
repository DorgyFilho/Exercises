#144 - Ida à Feira

N = int(input())

for i in range(N):
    qtdProd = int(input())

    cesta = {}

    for k in range(qtdProd):
        prod = input().split()
        nome = prod[0]
        preco = float(prod[1])
        cesta[nome] = preco

    total = 0.0
    p = int(input())
    for l in range(p):
        produto = input().split()
        P = produto[0]
        Q = int(produto[1])
        total += Q * cesta[P]
    print('R$ %.2f' %total)
