#113 - Matriz Quadrada III

while True:
    Num = int(input())
    if Num == 0:
        break
    
    M = []

    for a in range(Num):
        aux = []
        M.append(aux)
        for b in range(Num):
            M[a].append(0)
    
    M[0][0] = 1
    for k in range(0, Num):
        if k >= 1:
            M[k][0] = M[k-1][0]*2
    
        for l in range(1, Num):
            M[k][l] = M[k][l-1]*2

    
    T = len(str(M[Num-1][Num-1]))
    for r in range(Num):
        for s in range(Num):
            M[r][s] = str(M[r][s])
            while len(M[r][s]) < T:
                M[r][s] = ' ' + M[r][s]
        K = ' '.join(M[r])
        print(K)
    print()

