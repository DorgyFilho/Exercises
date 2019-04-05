#064 - Quadrante

while True:
    coord = input().split()
    X = int(coord[0])
    Y = int(coord[1])
    if X == 0 or Y == 0:
        break
    else:
        if X > 0 and Y > 0:
            print('primeiro')
        elif X < 0 and Y > 0:
            print('segundo')
        elif X < 0 and Y < 0:
            print('terceiro')
        elif X > 0 and Y < 0:
            print('quarto') 