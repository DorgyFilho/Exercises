#002 - Arquivo em Dicionário

Info = {}
arq = open(input('Digite o endereço do arquivo: '))
cont = arq.readlines()
arq.close()

for line in cont:
    linha = line.replace(' ', '')
    linha = line.split(' ')
    Info[linha[0]] = linha[1][:-1]
print(Info)
