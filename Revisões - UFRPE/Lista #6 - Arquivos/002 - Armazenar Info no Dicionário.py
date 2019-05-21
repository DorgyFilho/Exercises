#002 - Armazenar Info no Dicionário

nome = []
info = []
arq = open(input('Arquivo: '))
cont = arq.readlines()
arq.close()
for line in cont:
    linha = line.strip().split(' ')
    nome.append(linha[0])
    Nome = nome[:-1]
    info.append(linha)
    Info = info[:-1]
    
    data = zip(Nome, Info)

    agenda = {k: v for k,v in data}

print(agenda) 
    


