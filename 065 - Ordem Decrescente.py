#065 - Ordem Decrescente

x = int(input('Número a: '))
y = int(input('Número b: '))
z = int(input('Número c: '))

if (x > y and x > z):
    if y > z:
        print(x, y, z)
    else:
        print(x, y, z)
elif (y > x and y > z):
    if x > z:
        print(y, x, z)
    else:
        print(y, z, x)
elif (z > x and z > y):
    if x > y:
        print(z, x, y)
    else:
        print(z, y, x)
elif x == z or y == z or x == y:
    print('Há dois números iguais.')
