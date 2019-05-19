#007 - Atualizar Cadastro

agenda = {}
def cadastrar():
    while True:
        cpf = input('CPF: ')
        if cpf.lower() == 'fim':
            break
        nome = input('Seu Nome: ')
        curso = input('Curso: ')
        ende = input('Endereço: ')
        agenda[cpf] = {'Nome': nome, 'Curso': curso, 'Endereço': ende}

    print(agenda)
    print()

def alterar():
    global agenda
    Agenda = agenda
    busca = input('CPF: ')
    
    if busca in Agenda:
        opcao = input('Opção a ser alterada 1-Nome, 2-Curso, 3-Endereço: ')
        
        if opcao == '1':
            Agenda[busca]['Nome'] = input('Altere o seu nome: ')
            print(Agenda)

        elif opcao == '2':
            Agenda[busca]['Curso'] = input('Altere o curso: ')
            print(Agenda)
        
        elif opcao == '3':
            Agenda[busca]['Endereço'] = input('Altere seu endereço: ')
            print(Agenda)
        
        else:
            print('Opção Inválida!')
    

    else:
        print('Não Disponível!')

def imprimir():
    global agenda
    for k in agenda.items():
        print(k)

def Menu():
    global agenda
    while True:
        print('Bem-vindo(a)"\nOpções:\n1-Cadastrar\n2-Alterar\n3-Imprimir\n4-Sair')
        print()
        r = input('Opção: ')
        if r == '1':
            cadastrar()
        elif r == '2':
            alterar()
        elif r == '3':
            imprimir()
        elif r == '4':
            print('Volte sempre!')
            break

Menu()