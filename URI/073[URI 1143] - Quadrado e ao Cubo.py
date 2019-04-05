#073 - Quadrado e ao Cubo

N = int(input())

k = 1

for i in range(N):
    print('%d %d %d' %(k, k**2, k**3))
    k += 1