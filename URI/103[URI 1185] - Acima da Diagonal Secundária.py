#103 - Acima da Diagonal Secundária

SouM = input('').upper()
Matriz = []

for l in range(12):
    for c in range(12):
        valor = float(input(''))
        if l+c <= 10:
            Matriz.append(valor)

if SouM == 'S':
    print('%.1f' %sum(Matriz))
elif SouM == 'M':
    print('%.1f' %(sum(Matriz)/len(Matriz)))