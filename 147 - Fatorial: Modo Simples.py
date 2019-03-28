#147 - Fatorial: Modo Simples

fat = 1
num = int(input('Número: '))
valor = num

while valor > 0:
    fat *= valor
    valor -= 1
print(f'O fatorial de {num} é {fat}')
