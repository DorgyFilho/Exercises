#088 - Número Perfeito

N = int(input(''))

for k in range(N):
    soma = 0
    X = int(input(''))
    for y in range(1, X):
        if X%y == 0:
            soma += y
    
    if soma == X:
        print('%d eh perfeito' %X)
    else:
        print('%d nao eh perfeito' %X)
