#086 - Soma de Pares Consecutivos

while True:
    num = []
    X = int(input())
    if X == 0:
        break
    else:
        while len(num) != 5:
            if X % 2 == 0:
                num.append(X)
                X += 2
            else:
                X += 1
        print(sum(num))


