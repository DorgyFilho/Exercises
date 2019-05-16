#005 - Agenda

agenda = {}
cpf = ''
while cpf != 'fim':
    cpf = input('CPF: ')
    if cpf == 'fim':
        print('Cadastro Encerrado!')
        break        
    else:
        nome = input('Seu Nome: ')
        idade = input('Sua Idade: ')
        tel = input('Telefone: ')
        agenda[cpf] = {nome+'-'+idade+'-'+tel}

for k, v in agenda.items():
    print(f'{k}:{v}')  