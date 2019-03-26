#134 - Multiplicação Utilizando Apenas Soma e Subtração

n1 = int(input('Número a ser multiplicado: '))
n2 = int(input('Multiplicador: '))
res = 0
cont = 1
while cont <= n2:
    res += n1
    cont += 1
print(f'{n1} x {n2} = {res}')

