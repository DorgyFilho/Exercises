#004 - Maior e Menor Idades

Idades = [21,15,18,12,39,37,29,43,52,55,23,34,33,37,42,20,17,13,29,30]
menor = 1000
maior = 0

for i in Idades:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f'Menor: {menor} ---> Maior: {maior}')

