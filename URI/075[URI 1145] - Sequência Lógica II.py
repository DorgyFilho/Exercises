#075 - Sequência Lógica II

valor = input().split()
X = int(valor[0])
Y = int(valor[1])
div = Y//X
cont = 1
for i in range(1, div+1):
    k = ''
    for j in range(X):
        k += str(cont) + ' '
        cont += 1
    print(k[:-1])