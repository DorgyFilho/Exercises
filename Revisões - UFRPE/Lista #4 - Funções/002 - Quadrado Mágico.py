#002 - Quadrado Mágico

from random import randint

def mQuadrada(M):
    tam = len(M)
    listaSoma = [] 
    #Parte Horizontal
    listaSoma.extend(sum(line) for line in M) 
    #Parte vertical
    for col in range(tam):
        listaSoma.append(sum(lin[col] for lin in M))
    #Diagonais
    res1 = 0
    for d in range(0, tam):
        res1 += M[d][d]
        listaSoma.append(res1)
    res2 = 0
    for k in range(tam-1, -1, -1):
        res2 += M[k][k]
        listaSoma.append(res2)
    if len(set(listaSoma)) > 1:
        return 'Não é um quadrado mágico'
    return 'É um quadrado mágico'

def result(M):
    Retorno = mQuadrada(M)
    return Retorno


M = []
lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    aux = []
    for c in range(1, col+1):
        pos = randint(1,100)
        aux.append(pos)
    M.append(aux)

resultado = result(M)
print(resultado)



