#009 - Palavras Simultâneas

a = open(input('Arquivo 1: '))
a2 = open(input('Arquivo 2: '))
rep = open(input('Arquivo 3: '), 'w')

def limpa(texto):
    P = ['.', ',', '?', '!', '(', ')', '  ']
    for ponto in P:
        texto = texto.replace(ponto, '')
    return texto

def busca(LP):
    mais3 = []
    for word in LP:
        if len(word) > 3:
            mais3.append(word)
    return mais3

Info = a.read()
Info = limpa(Info)
LP1 = Info.split(' ')
LP1 = busca(LP1)
Inf2 = a2.read()
Inf2 = limpa(Inf2)
LP2 = Inf2.split(' ')
LP2 = busca(LP2)

Dados = {}
for rose in LP1:
    Dados[rose] = None

for mark in LP2:
    if mark in Dados:
        rep.write(mark + '\n')

a.close()
a2.close()
rep.close()


