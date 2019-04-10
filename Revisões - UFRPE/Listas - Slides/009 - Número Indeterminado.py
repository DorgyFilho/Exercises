#009 - Número Indeterminado

numero = []
qtde = 0

while True:
    num = float(input('Número: '))
    if num == 0:
        break
    else:
        numero.append(num)

tam = len(numero)
soma = sum(numero)
media = soma/tam

acimaMedia = []
for k in numero:
    if k > media:
        acimaMedia.append(k)

tamAcima = len(acimaMedia)
print(f'Quantidade de Notas: {tam}')
print(f'{numero}')
numero.reverse()
print(f'Soma: {soma:.2f}')
print(f'Média: {media:.2f}')
print(f'Quantidade de Notas Acima da Média: {tamAcima}')

for y in numero:
    print(y)





