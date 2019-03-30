#013 - Dividir Apenas Com Adição e Subtração

a = int(input('Dividendo: '))
b = int(input('Divisor: '))
quo = 0
while b <= a:
    a -= b
    quo += 1

print(f'Resultado da divisão: {quo}')

'''O resultado da divisão corresponde a quantidade
de vezes necessária para o divisor deduzir o seu valor do dividendo.
'''