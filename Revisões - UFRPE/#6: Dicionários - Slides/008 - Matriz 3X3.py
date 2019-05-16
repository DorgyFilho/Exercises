#008 - Matriz 3x3

from random import randint

def imprimir(M):
    for k in range(1,4):
        aux = ''
        for l in range(1,4):
            aux += str(M[(k,l)]) + ' '
        print(aux)

Mat = {}
P = 0
I = 0
for l in range(1,4):
    for c in range(1,4):
        Mat[(l,c)] = randint(0,9)

for l in range(1,4):
    for c in range(1,4):        
        if Mat[(l,c)] % 2 == 0:
            P += Mat[(l,c)]
        else:
            I += Mat[(l,c)]

imprimir(Mat)
print(f'Total Pares: {P}\nTotal Ímpares: {I}')

