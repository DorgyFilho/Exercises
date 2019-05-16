#004 - Divisão Apenas Com Adição e Subtração

a = int(input('Dividendo: '))
k = int(input('Divisor: '))
quo = 0
d = a

while k <= d:
    d -= k
    quo += 1
print(f'{a} / {k} = {quo}')