#059 - Preço de Três Produtos - Escolher o mais barato
p1 = float(input('Preço do Produto 1: '))
p2 = float(input('Preço do Produto 2: '))
p3 = float(input('Preço do Produto 3: '))

if p1 > p2 > p3:
    print(f'Mais Barato: R${p3}')
elif p1 > p3 > p2:
    print(f'Mais Barato: R${p2}')
elif p2 > p3 > p1:
    print(f'Mais Barato: R${p1}')
elif p2 > p1 > p3:
    print(f'Mais Barato: R${p3}')
elif p3 > p2 > p1:
    print(f'Mais Barato: R${p1}')
elif p3 > p1 > p2:
    print(f'Mais Barato: R${p2}')