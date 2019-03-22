#103 - Número Primo 3

n = int(input('Número: '))
cont = 0
div = 0
for i in range(1, n+1):
    if n % i == 0:
        cont += 1
        div += 1
if cont <= 2:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')
    n -= 1
print(f'Número de divisões: {div}')
