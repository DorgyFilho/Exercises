#008 - Nome Invertido

def nomeInv(nome):
    invertido = ''
    for i in nome:
        invertido = i + invertido
    return invertido.upper()
