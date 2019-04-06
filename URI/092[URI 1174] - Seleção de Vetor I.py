#092 - Seleção Em Vetor I

A = []
for i in range(100):
    X = float(input(''))
    A.append(X)

for i in range(100):
    if A[i] <= 10:
        print('A[%d] = %.1f' %(i, A[i]))

