#085 - Soma de ímpares Consecutivos III

cont = 0
qtde = int(input())
while cont < qtde:
    N = input().split()
    X = int(N[0])
    Y = int(N[1])
    cont2 = 0
    numeros = []
    if X % 2 == 0:
        X += 1
    while cont2 < Y:
        numeros.append(X)
        cont2 += 1
        X += 2
    print(sum(numeros))
    cont += 1




