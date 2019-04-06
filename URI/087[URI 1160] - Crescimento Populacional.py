#087 - Crescimento Populacional

qtde = int(input())

for i in range(qtde):
    v = input().split()
    PA = int(v[0])
    PB = int(v[1])
    G1 = float(v[2])
    G2 = float(v[3])

    anos = 0

    while PA <= PB:
        cPA = int((G1/100)*PA)
        cPB = int((G2/100)*PB)
        anos += 1
        PA += cPA
        PB += cPB

        if anos > 100:
            break
    
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('%d anos.' %anos)


