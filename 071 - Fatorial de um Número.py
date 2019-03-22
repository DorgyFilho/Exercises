#071 - Fatorial de um número

fat = 1
num = ''
num = int(input('Digite um número: '))
if num == 20:
    print('Entrada inválida!')
valor = num

print(f'{valor}! = ', end=' ')
while valor > 0:
    print(f'{valor}', end=' ')
    print('.' if valor > 1 else '=', end=' ')
    fat *= valor
    valor -= 1
print(f'{fat}')