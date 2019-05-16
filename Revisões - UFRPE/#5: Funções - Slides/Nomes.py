#006 - Nomes

def lerLista(lNome):
    for item in lNome:
        print(item)
    return ''

def CoMa(lNome):
    nomesCoMa = []
    for nome in lNome:
        if nome.startswith('a'):
            nomesCoMa.append(nome)
    return nomesCoMa

def imprimir(lNome):
    lista = CoMa(lNome)
    return lista

    
    
    
