#076 - Somando Inteiros Consecutivos

L = list(map(int, input().split()))
i = 1
soma = 0

while L[i] <= 0:
    if L[i] <= 0:
        i += 1
    if L[i] > 0:
        break

for k in range(0, L[i]):
    soma = soma + L[0] + k
print(soma)
