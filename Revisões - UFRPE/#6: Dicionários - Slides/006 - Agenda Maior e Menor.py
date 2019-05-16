#006 - Agenda Maior e Menor

agenda = {}
while True:
    cpf = input('Seu CPF: ')
    if cpf == 'fim':
        print('Cadastro Encerrado!')
        print()
        break
    else:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        agenda[cpf] = {'Nome':nome, 'Idade':idade}

menorde18 = {}
listaMenores = []
for valor in agenda:
    if agenda[valor]['Idade'] < 18:
        listaMenores.append(valor)

for cpf in listaMenores:
    menorde18[cpf] = agenda.pop(cpf)

print('Maiores:')
print()
for CPF in agenda:
    print(f"CPF: {CPF}, Nome: {agenda[CPF]['Nome']}, Idade:{agenda[CPF]['Idade']}")
print()
print('Menores:')
print()
for Cpf in menorde18:
    print(f"CPF: {Cpf}, Nome: {menorde18[Cpf]['Nome']}, Idade:{menorde18[Cpf]['Idade']}")

