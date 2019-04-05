#066 - Validação de Nota

media = 0
cont = 0
soma = 0
while cont < 2:
    nota = float(input(''))
    if nota >= 0.0 and nota <= 10.0:
        soma += nota
        cont += 1
        media = soma/2
    else:
        print('nota invalida')

print('media = %.2f' %media)

