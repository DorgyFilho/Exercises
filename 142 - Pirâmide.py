#142 - Pirâmide de estrela na horizontal

#1 - Metade superior
n = 10
for i in range(n):
    for k in range(i):
        print('*', end='')
    print()

#2 - Metade Inferior
for i in range(n, 0, -1):
    for k in range(i):
        print('*', end='')
    print()