#187 - Abreviações

while True:
    abr = {}
    frase = input().replace('\n','').replace('\r','')
    if frase == '.':
        break
    else:
        cont = frase.split(' ')
        for w in cont:
            if len(w) > 2:
                primeiro = w[0]
                if primeiro not in abr:
                    abr[primeiro] = w
                else:
                    contarP = cont.count(w)
                    economizarP = contarP * (len(w)-2)
                    contarAnterior = cont.count(abr[primeiro])
                    economizarAnterior = contarAnterior*len(abr[primeiro]) - 2
                    if economizarAnterior < economizarP:
                        abr[primeiro] = w
        
    forma = ''
    qtdeAbr = 0
    for add in cont:
        primeiro = add[0]
        if primeiro in abr and add == abr[primeiro]:
            forma += primeiro + '. '
            if 'a' in forma:
                qtdeAbr = 1
            else:
                qtdeAbr += 1
        else:
            forma += add + ' '

       
    resultado = ''
    print(forma)
    print(qtdeAbr)
    abrev = list(abr.keys())
    abrev.sort()
    for chave in abrev:
        resultado += chave + '.' + ' = ' + abr[chave] + ' ' + '\n'
    print(resultado[:-1])



