#064 - Ano Bissexto

ano  = int(input('Digite o ano a ser consultado - Ex: 2019: '))
if ano < 1000 or ano > 9999:
    print('Ano Inválido!')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')
