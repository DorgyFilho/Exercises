#001 - Vogais e Consoantes

arquivo = open(input('Digite o endereço do seu arquivo: '))
cont = arquivo.readlines()
arquivo.close()

vogais = ''
conso = ''

for nome in cont:
    if nome.startswith('A') or nome.startswith('a') or nome.startswith('E') or nome.startswith('e') or nome.startswith('I') or nome.startswith('i') or nome.startswith('O') or nome.startswith('o') or nome.startswith('U') or nome.startswith('u'):
        vogais += nome + '\n'
    else:
        conso += nome + '\n'

vog = open(input('Digite o caminho do arquivo a ser salvo junto com o nome: '), 'w')
con = open(input('Digite o caminho do arquivo a ser salvo junto com o nome: '), 'w')
vog.writelines(vogais)
con.writelines(conso)
vog.close()
con.close()



