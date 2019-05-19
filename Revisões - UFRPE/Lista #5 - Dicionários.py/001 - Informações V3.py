#001 - Informações V3
#Mostrar o usuário que possui a maior idade

agenda = {}
maisVelho = 0
while True:
    CPF = input('CPF: ')
    if CPF.lower() == 'fim':
        break
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    tel = input('Telefone: ')
    if idade > maisVelho:
        maisVelho = idade
        PessoaMV = nome
        TelVelho = tel
        CPFMaisVelho = CPF 
        agenda[CPFMaisVelho] = {'Nome': PessoaMV, 'Idade': maisVelho, 'Telefone': TelVelho, 'CPF': CPFMaisVelho}
        Agenda = agenda[CPFMaisVelho]


print(Agenda)






            

    
        






