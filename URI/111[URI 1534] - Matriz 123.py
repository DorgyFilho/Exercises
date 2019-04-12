#111 - Matriz 123

while True:
    try:
        ent = int(input(''))
    
        Num = []

        col = ent-1
        for l in range(ent):
            aux = []
            for c in range(ent):
                if c == col:
                    aux.append(2)
                    col -= 1
                else:
                    if l == c:
                        aux.append(1)
                    else:
                        aux.append(3)
            Num.append(aux)
    
        for x in range(ent):
            res = ''
            for y in range(ent):
                res += str(Num[x][y])
            print(res)
    except EOFError:
        break        