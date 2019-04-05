#047 - Soma De Ímpares Consecutivos I

X = int(input(''))
Y = int(input(''))
somaImpares = 0

for i in range(Y+1, X):
    if i % 2 != 0:
        somaImpares += i

print(somaImpares)
        