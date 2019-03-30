#001 - Idade e Altura

altura = ''
qtdAlunos = 0
while altura != 0:
    altura = float(input('Altura: '))
    if altura == 0:
        print('Cadastro Encerrado!')
        break
    idade = int(input('Idade: '))
    if idade > 13 and altura < 1.5:
        qtdAlunos += 1

print(f'Quantidade de Alunos Maiores de 13 anos com altura inferior à 1.50 m: {qtdAlunos}')

    