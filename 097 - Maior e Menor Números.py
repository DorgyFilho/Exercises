#097 - Maior e Menor Números

maior = 0
menor = 9999
somaMaiorMenor = 0


inicio = int(input('Número Inicial: '))
fim = int(input('Número Final: '))

for i in range(inicio, fim+1):
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    somaMaiorMenor = maior + menor

print(f'Maior: {maior}\nMenor: {menor}\nSoma Entre o Maior e o Menor: {somaMaiorMenor}')
