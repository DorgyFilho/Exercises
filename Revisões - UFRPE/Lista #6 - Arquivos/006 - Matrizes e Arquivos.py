#006 - Matrizes e Arquivos

arq = open(input('Arquivo: '), 'w')

matriz = []
lin = int(input('Linha: '))
col = int(input('Coluna: '))

for l in range(1, lin+1):
    aux = []
    for c in range(1, col+1):
        elem = int(input(f'Posição {l}, {c}: '))
        aux.append(elem)
    matriz.append(aux)

for a in matriz:
    for b in a:
        arq.writelines(str(b))
        arq.writelines(' ')
    arq.writelines('\n')

arq.close()