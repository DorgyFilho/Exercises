#069 - Idade e Altura

altura = ''
maisDe13Alt = 0
while altura != 0:
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    if altura == 0:
        print('Cadastro Encerrado!')
        break
    if idade > 13 and altura < 1.5:
        maisDe13Alt += 1

print(f'Pessoas maiores de 13 anos com altura inferior a 1.50: {maisDe13Alt}')

