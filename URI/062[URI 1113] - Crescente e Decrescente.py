#062 - Crescente e Decrescente

while True:
    valor = input().split()
    X = int(valor[0])
    Y = int(valor[1])
    if X == Y:
        break
    else:
        if X > Y:
            print('Decrescente')
        elif X < Y:
            print('Crescente')
