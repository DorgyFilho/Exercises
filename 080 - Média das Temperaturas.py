#080 - Temperaturas

qtdTemp = 0
somaTemp = 0
maiorTemp = 0
menorTemp = 1000
for i in range(1,5):
    temp = float(input('Temperatura: '))
    qtdTemp += 1
    somaTemp += temp
    if temp > maiorTemp:
        maiorTemp = temp
    if temp < menorTemp:
        menorTemp = temp

mediaTemp = somaTemp/qtdTemp

print(f'Menor Temperatura: {menorTemp:.2f}°C')
print(f'Maior Temperatura: {maiorTemp:.2f}°C')
print(f'Média das Temperaturas: {mediaTemp:.2f}°C')