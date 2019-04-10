#109 - Matriz Quadrada

while True:
    ent = int(input())
    if ent == 0:
        break
    numero = []
    for i in range(ent):
        linha = []
        for j in range(ent):
            linha.append(1)
        numero.append(linha)
    
    k = 1
    c = 0
    e = 0
    b = ent - 1
    d = ent - 1
    
    if ent % 2 == 0:
        m = ent/2
    else:
        m = (ent+1)/2
    
    while k <= m:
        a = e
        while a <= d:
            numero[c][a] = k
            numero[b][a] = k
            a += 1

        a = c + 1
        while a < b:
            numero[a][e] = k
            numero[a][d] = k
            a += 1
        
        k += 1
        c += 1
        b -= 1
        e += 1
        d -= 1
    
    for t in range(ent):
        texto = ''
        for j in range(ent):
            texto += ' %3d' %numero[t][j]
        print(texto[1:])
    print('')
