#004 - Informações Ordenadas Pela Chave

Info = {}

nome = input('Nome: ')
idade = input('Idade: ')
tel = input('Telefone: ')
endereco = input('Endereço: ')

Info['Nome'] = nome
Info['Idade'] = idade
Info['Telefone'] = tel
Info['Endereço'] = endereco

for key in sorted(Info):
    print(f'{key}:{Info[key]}')