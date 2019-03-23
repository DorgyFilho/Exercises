#113 - Maior e Menor Temperatura

soma = 0
media = 0
maiorTemp = 0
menorTemp = 1000
nTemp = int(input('Número de temperaturas: '))

for i in range(1, nTemp+1):
    temp = float(input(f'Digite a {i}° temperatura: '))
    soma += temp
    if temp > maiorTemp:
        maiorTemp = temp
    if temp < menorTemp:
        menorTemp = temp
    media = soma/i

print()
print(f'Soma das Temperaturas: {soma:.2f}°C')
print()
print(f'Média das Temperaturas: {media:.2f}°C')
print()
print(f'Maior Temperatura: {maiorTemp}°C')
print()
print(f'Menor Temperatura: {menorTemp}°C')
