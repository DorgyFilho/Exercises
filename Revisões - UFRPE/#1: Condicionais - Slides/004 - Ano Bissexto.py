#004 - O ano é bissexto?

ano = int(input('Digite o ano a partir de 1000: '))
if ano < 1000:
    print('Inválido! Apenas números com 4 dígitos são permitidos.')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{ano} é um ano bissexto.')
    else:
        print(f'{ano} não é um ano bissexto.')
