#009 - Referência Acadêmica

nCom = input('Nome Completo: ').upper()

nome = nCom.split()

qtde = len(nome)

if qtde == 2: #Sobrenome, nome
    print(f'{nome[-1]}, {nome[0][0]}')
elif qtde > 2: 
    print(f'{nome[qtde-1]}, {nome[0][0]}.{nome[-2][0]}')
else:
    print(f'{nCom}')
    
