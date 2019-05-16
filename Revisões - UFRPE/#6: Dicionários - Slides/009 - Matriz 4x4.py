#009 - Matriz 4x4

from random import randint

def imprime(M):
    for x in range(4):
        aux = ''
        for y in range(4):
            aux += ('%.2d '%(M[x,y]))
        print(aux)

Mat = {}
for k in range(4):
     for l in range(4):
         Mat[(k,l)] = randint(0,99)
imprime(Mat)

for c in range(4):
    aux2 =  Mat[(1,c)]
    Mat[(1,c)] = Mat[(2,c)] 
    Mat[(2,c)] = aux2
print('Matriz depois da troca de linha')
imprime(Mat)

for l in range(4):
    aux3 = Mat[(l,1)] 
    Mat[(l,1)] = Mat[(l,2)] 
    Mat[(l,2)] = aux3
print('Matriz depois da troca de coluna')
imprime(Mat)



