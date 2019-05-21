#004 - Nomes Que Começam Com Vogal

arq = open(input('Arquivo: '))
Nomes = arq.readlines()
arq.close()

arq = open(input('Arquivo: '), 'w')
for n in Nomes:
    if n.startswith('A') or n.startswith('a') or n.startswith('E') or n.startswith('e') or n.startswith('I') or n.startswith('i') or n.startswith('O') or n.startswith('o') or n.startswith('U') or n.startswith('u'):
        arq.writelines(n+'\n')

arq.close()