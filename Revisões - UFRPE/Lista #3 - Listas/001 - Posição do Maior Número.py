#001 - Posição do Maior Número

Num = []

for i in range(8):
    num = int(input(f'{i}° número: '))
    Num.append(num)

maior = max(Num)
posMaior = Num.index(maior)

print(f'Posição: {posMaior} ---> Maior Número: {maior}')

