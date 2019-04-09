#101 - Acima da Diagonal Principal.

SomaOuMedia = input('')
Matriz = []

for l in range(12):
    for c in range(12):
        pos = float(input(''))
        if l < c:
            Matriz.append(pos)

if SomaOuMedia == 'S':
    print('%.1f' %(sum(Matriz)))
elif SomaOuMedia == 'M':
    print('%.1f' %(sum(Matriz)/len(Matriz)))
