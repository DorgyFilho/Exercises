#005 - Aritmética Modular: Resto da Divisão Apenas Com Adição e Subtração

a = int(input('Dividendo: '))
k = int(input('Divisor: '))
d = a
quo = 0
resto = 0

while k <= d:
    d -= k
    quo += 1
    resto = d
print(f'{a}/{k} = {quo} --> Resto da Divisão: {resto}')
