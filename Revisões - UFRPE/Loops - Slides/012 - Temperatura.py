#012 - Temperatura

menorTemp = 10000
maiorTemp = 0
somaTemp = 0
mediaTemp = 0
qtdTemp = 0

for i in range(1,6):
    temp = float(input(f'{i}° Temperatura: '))

    if temp > maiorTemp:
        maiorTemp = temp
    
    if temp < menorTemp:
        menorTemp = temp

    somaTemp += temp
    qtdTemp += 1

mediaTemp = somaTemp/qtdTemp

print(f'Quantidade de Temperaturas: {qtdTemp}')
print(f'Maior Temperatura: {maiorTemp}°C')
print(f'Menor Temperatura: {menorTemp}°C')
print(f'Soma das Temperaturas: {somaTemp}°C')
print(f'Média das Temperaturas: {mediaTemp:.2f}°C')
