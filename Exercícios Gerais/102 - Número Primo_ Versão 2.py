#102 - Número Primo: Divisores

n = int(input('Número: '))
cont = 0
div = []
for i in range(n):
    if n % (i+1) == 0:
        cont += 1
        div.append(i+1)
    else:
        cont

if cont == 2:
    print(f'{n} é primo, pois é divisível por {div}')
else:
    print(f'Não é primo, pois é divisível por {div}')
