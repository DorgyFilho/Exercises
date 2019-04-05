#046 - Seis Números Ímpares

X = int(input(''))

if X % 2 == 0:
    X += 1

for i in range(X, X+12, 2):
    print(i)
