#002 - Média Aritmética

Num = []

for i in range(20):
    num = float(input(f'Numero {i+1}: '))
    Num.append(num)

media = sum(Num)/len(Num)

abaixoMedia = []
for j in Num:
    if j < media:
        abaixoMedia.append(j)

print(f'Média: {media:.2f}')
print(f'Valores abaixo da média: {abaixoMedia}')
