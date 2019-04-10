#006 - Média das Temperauras e Acima da Média

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

Temp = []

for i in range(12):
    temp = float(input(f'Temperatura do mês de {mes[i]}: '))
    Temp.append(temp)

media = sum(Temp)/12

acimaMedia = []
for j in Temp:
    if j > media:
        acimaMedia.append(j)

mesAcima = []
for k in range(len(mes)):
    if Temp[k] > media:
        mesAcima.append(mes[k])

print(f'Média: {media:.2f}º')
print(mesAcima)
print(acimaMedia)
