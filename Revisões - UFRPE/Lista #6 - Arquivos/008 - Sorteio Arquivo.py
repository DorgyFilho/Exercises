#008 - Sorteio Arquivo

from random import choice

arq = open(input('Arquivo: '))
nomes = arq.readlines()
arq.close()
escolhido = choice(nomes)

Win = open(input('Arquivo do vencedor: '), 'w')
Win.write(escolhido)
Win.close()
