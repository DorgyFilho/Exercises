#179 - Desafio Arquivos

import os

atual = os.getcwd()
arq = os.listdir(atual)
print(arq)
Final = 'resultado.txt'
if Final in arq:
    arq.remove(Final)

busca = input('Busca: ')
ArqFim = open(Final, 'w', encoding='utf-8')
for f in arq:
    arq = open(f, encoding='utf-8')
    cont = arq.read().lower()
    cont = cont.replace('  ', ' ')
    qtd = cont.count(busca)
    ArqFim.write('%s - %d vez(es)\n' %(f, qtd))
    arq.close()
ArqFim.close()

