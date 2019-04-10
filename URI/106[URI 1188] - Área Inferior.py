#106 - Área Inferior

M = []
SouM = input('').upper()

for l in range(12):
    for c in range(12):
        valor = float(input(''))
        if l >= 7 and l+c >= 12 and c < l:
            M.append(valor)

if SouM == 'S':
    print('%.1f' %sum(M))
elif SouM == 'M':
    print('%.1f' %(sum(M)/len(M)))