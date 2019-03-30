#057 - Maior Entre Três Números

a = int(input('1° Número: '))
b = int(input('2° Número: '))
c = int(input('3° Número: '))

if a > b and a > c:
    print(f'O maior número é a: {a}')
elif b > a and b > c:
    print(f'O maior número é b: {b}')
elif c > a and c > b:
    print(f'O maior número é c: {c}')
