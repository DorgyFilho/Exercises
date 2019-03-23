#112 - Fatorial [Versão Sem Limites]

num = int(input('Digite o valor a ser calculado: '))
fat = 1
valor = num

print(f'Fatorial de {num}! = ', end=' ')
while valor > 0:
    print(f'{valor}', end=' ')
    print('.' if valor > 1 else '=', end=' ')
    fat *= valor
    valor -= 1
print(f'{fat}')