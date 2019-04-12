#010 - Multiplicação Entre Matrizes

A = []
B = []
M = []

Lin = int(input('Linha: '))
Col = int(input('Coluna: '))
L = int(input('Linha: '))
C = int(input('Coluna: '))

if Lin == C:
    for l in range(1, Lin+1):
        aux = []
        for c in range(1, Col+1):
            valor = int(input('Valor: '))
            aux.append(valor)
        A.append(aux)

    for lin in range(1, L+1):
        aux2 = []
        for col in range(1, C+1):
            V = int(input('Valor: '))
            aux2.append(V)
        B.append(aux2)


    for a in range(len(A)):
        multi = []
        for b in range(len(B[0])):
            K = 0
            for t in range(len(A[0])):
                K += A[a][t]*B[t][b]
            multi.append(K)
        M.append(multi)

    for r in M:
        for s in r:
            print(s, end=' ')
        print()

else:
    print('Inválida!')




