#071 - Fatorial de um número

fat = 1
while True:
    num = int(input('Digite um número: '))
    if num >= 20:
        print('Entrada inválida!')
        continue
    else:
        valor = num

    print(f'{valor}! = ', end=' ')
    while valor > 0:
        print(f'{valor}', end=' ')
        print('.' if valor > 1 else '=', end=' ')
        fat *= valor
        valor -= 1
    print(f'{fat}')
    break