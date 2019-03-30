#058 - Maior e Menor Entre Trẽs Números

a = int(input('Número a: '))
b = int(input('Número b: '))
c = int(input('Número c: '))

if a > b > c:
    print(f'Maior Número: {a}\nMenor Número: {c}')
elif a > c > b:
    print(f'Maior Número: {a}\nMenor Número: {b}')
elif b > c > a:
    print(f'Maior Número: {b}\nMenor Número: {a}')
elif b > a > c:
    print(f'Maior Número: {b}\nMenor Número: {c}')
elif c > b > a:
    print(f'Maior Número: {c}\nMenor Número: {a}')
elif c > a > b:
    print(f'Maior Número: {c}\nMenor Número: {b}') 
       