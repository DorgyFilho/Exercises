#078 - Ultrapassando Z

X = int(input(''))
Z = 0
soma = 0
k = 0

while Z <= X:
    Z = int(input(''))
    if Z > X:
        break

while X <= Z:
    X += 1
    soma += X
    k += 1
    if soma > Z:
        break

print(k)

