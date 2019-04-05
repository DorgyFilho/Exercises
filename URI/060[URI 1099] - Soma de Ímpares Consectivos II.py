#060 - Soma de Ímpares Consecutivos

N = int(input(''))

for i in range(N):
    valor = input().split()
    X = int(valor[0])
    Y = int(valor[1])
    somaImpares = 0

    if X == Y:
        print(0)
    else:
        Z = 0
        if X > Y:
            Z = X
            X = Y
            Y = Z
        
        while X < (Y-1):
            X += 1
            if X % 2 != 0:
                somaImpares += X
    
        print(somaImpares)

        

