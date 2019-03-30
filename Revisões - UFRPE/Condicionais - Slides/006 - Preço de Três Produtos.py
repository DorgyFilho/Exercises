#006 - Preço de Três Produtos e Mostrar o Mais Barato

x = float(input('Preço 1: '))
y = float(input('Preço 2: '))
z = float(input('Preço 3: '))
maisBarato = 0

if x < y and x < z:
    maisBarato = x
    print(f'O produto mais barato custa R${x:.2f}')
elif y < x and y < z:
    maisBarato = y
    print(f'O produto mais barato custa R${y:.2f}')
elif z < x and z < y:
    maisBarato = z
    print(f'O produto mais barato custa R${z:.2f}')

