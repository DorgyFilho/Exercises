#065 - Dividindo X Por Y

N = int(input(''))

for i in range(N):
    valor = input().split()
    X = int(valor[0])
    Y = int(valor[1])
    if Y == 0:
        print('divisao impossivel')
    else:
        div = X/Y
        print(div)
