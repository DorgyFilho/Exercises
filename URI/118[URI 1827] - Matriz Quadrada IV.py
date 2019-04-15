#118 - Matriz Quadrada IV

while True:
    try:
        K = int(input())
        L = int(K/3)
        T = K - L

        #Preencher com 0
        M = [[0 for a in range(K)] for b in range(K)]

        #Preencher com 2
        for d in range(K):
            M[d][d] = 2
        
        #Preencher com 3
        y = 0
        for f in range(K-1,-1,-1):
            M[y][f] = 3
            y += 1
        
        #Preencher o meio com 1
        for m in range(L, T):
            for n in range(L, T):
                M[m][n] = 1
        
        M[int(K/2)][int(K/2)] = 4

        for v in range(K):
            for w in range(K):
                print(M[w][v], end='')
            print()
        print()

    
    except EOFError:
        break

