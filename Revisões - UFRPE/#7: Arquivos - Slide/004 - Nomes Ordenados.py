#004 - Nomes Ordenados

arq = open(input('Digite o endereço de seu arquivo: '))
conteudo = arq.readlines()
arq.close()

Ordem = sorted(conteudo)

Ord = open(input('Digite o arquivo a ser criado com o endereço: '), 'w')
Ordenado = ''
for nome in Ordem:
    nomes = nome.split('\n')
    
    for n in nomes:
        Ordenado += n+'\n'

Ord.writelines(Ordenado)
        
Ord.close()