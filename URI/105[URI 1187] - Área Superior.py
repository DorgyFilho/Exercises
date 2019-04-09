#105 - Área Superior

SouM = input('').upper()
total = 0
contador = 0

for l in range(12):
    for c in range(12):
        valor = float(input(''))
        if c-l >= 1 and c+l <= 10:
            total += valor
            contador += 1
    if l == 5:
        break

if SouM == 'S':
    print('%.1f' %total)
if SouM == 'M':
    print('%.1f' %(total/contador))
