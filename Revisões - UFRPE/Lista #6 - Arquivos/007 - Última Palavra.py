#007 - Última Palavra

arq = open(input('Arquivo: '))
conteudo = arq.readlines()
ultimo = conteudo[-1]
arq.close()
print(ultimo)
