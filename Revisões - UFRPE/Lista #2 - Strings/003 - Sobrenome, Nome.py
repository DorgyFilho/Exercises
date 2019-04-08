#003 - Sobrenome, Nome

nCom = input('Nome Completo: ')
nome = nCom.split()
qtde = len(nome)

if qtde == 2:  #Sobrenome, Nome
    print(f'{nome[-1]}, {nome[0]}')
elif qtde > 2:
    print(f'{nome[qtde-1]}, {nome[0]}')
else:
    print(f'{nCom}')
    
