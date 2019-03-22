#092 - Soma dos Números de Um Determinado Intervalo.

soma = 0
inicio = int(input('Número Inicial: '))
fim = int(input('Número Final: '))

for i in range(inicio+1, fim):
    soma += i
print(f'A soma é {soma}')
