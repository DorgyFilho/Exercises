#030 - Peso Ideal 2

altura = float(input('Altura: '))
sexo = input('Sexo - M ou F: ').upper()
if sexo == 'M':
    pIdeal = (72.7*altura) - 58
elif sexo == 'F':
    pIdeal = (62.1*altura) - 44.7
else:
    print('Erro! Informação Inválida!')
    altura = 0
    sexo = 'Inválido'
    pIdeal = 0

print(f'Altura: {altura:.2f}\nSexo: {sexo}\nPeso Ideal: {pIdeal:.2f} kg')
