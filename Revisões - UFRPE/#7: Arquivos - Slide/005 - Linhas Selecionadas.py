#005 - Linhas Selecionadas

arq = open(input('Endereço do seu arquivo: '))
cont = arq.readlines()[3:6]
arq.close()

Nomes = open(input('Crie um arquivo digitando o seu endereço: '), 'w')
for nome in cont:
    Nomes.writelines(nome)

Nomes.close()
