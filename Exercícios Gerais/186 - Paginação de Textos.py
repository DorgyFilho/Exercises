#186 - Paginação de Textos

CMAX = 76
L = 60
def paginas(arq, l, pag):
    if l == L:
        ultimo = 'Texto --- %d' %pag
        arq.write(ultimo.center(L-1)+'\n')
        pag += 1
        l = 1
    return l, pag

def escreverTexto(arq, l, nLin, pag):
    arq.write(l+'\n')
    return paginas(arq, nLin+1, pag)

entrada = open(input('Arquivo de entrada: '))
saida = open(input('Arquivo de destino: '), 'w')
conteudo = entrada.readlines()
entrada.close()

Pag = 1
Lin = 1

for l in conteudo:
    Info = l.rstrip().split(' ')
    l = ''
    for elem in Info:
        elem = elem.strip()
        if len(l) + len(elem)+1 > L:
            Lin, Pag = escreverTexto(saida, l, Lin, Pag)
            l = ''
        l += elem+' '  
    if l != '':
        Lin, Pag = escreverTexto(saida, l, Lin, Pag)

while Lin != 1:
    Lin, Pag = escreverTexto(saida, '', Lin, Pag)

saida.close()









