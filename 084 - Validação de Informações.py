#084 - Validação de Informações

while True:
    nome = input('Digite o seu nome: ')
    if len(nome) <= 3:
        print('Nome inválido. Caracteres abaixo ou igual a 3. Tente novamente.')
        continue
    idade = int(input('Digite a sua idade: '))
    if not (0 <= idade <= 150):
        print('Idade inválida. Tente novamente.')
        continue
    salario = float(input('Digite o seu salário: '))
    if salario <= 0:
        print('Salário inválido. Tente novamente.')
        continue
    sexo = input('Digite o seu sexo: ')
    if not (sexo == 'm' or sexo == 'f'):
        print('Informação inválida. Tente novamente.')
        continue
    else:
        print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario:.2f}\nSexo: {sexo}')
        break
