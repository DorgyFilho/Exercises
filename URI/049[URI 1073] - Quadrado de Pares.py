#049 - Quadrado de Pares

N = int(input(''))

for i in range(1, N+1):
    if i % 2 == 0:
        res = i**2
        print('%d^2 = %d' %(i, res))
