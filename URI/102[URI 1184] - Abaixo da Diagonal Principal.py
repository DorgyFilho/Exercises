#102 - Abaixo da Diagonal Principal

SouM = input('').upper()
Matriz = []

for l in range(12):
    for c in range(12):
        pos = float(input())
        if l > c:
            Matriz.append(pos)

if SouM == 'S':
    print('%.1f' %sum(Matriz))
elif SouM == 'M':
    print('%.1f' %(sum(Matriz)/len(Matriz)))