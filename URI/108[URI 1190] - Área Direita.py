#108 - Área Direita

M = []
SouM = input('').upper()

for l in range(12):
    for c in range(12):
        num = float(input(''))
        if l + c >= 12 and c - l >= 1:
            M.append(num)

if SouM == 'S':
    print('%.1f' %sum(M))
elif SouM == 'M':
    print('%.1f' %(sum(M)/len(M)))
