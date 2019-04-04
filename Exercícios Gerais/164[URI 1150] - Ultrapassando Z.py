#164 - Ultrapassando Z

X = int(input(''))
Z = 0
cont = 0
soma = 0

while Z <= X:
    Z = int(input(''))
    if Z > X:
        break

while X < Z:
    X += 1
    soma += X
    cont += 1
    if soma > Z:
        break

print(cont)
