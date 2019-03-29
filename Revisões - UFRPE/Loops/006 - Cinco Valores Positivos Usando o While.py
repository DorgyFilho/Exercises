#006 - Cinco Valores Positivos Usando o While

qtd = 0
while qtd < 5:
    num = int(input('Número: '))
    if num < 0:
        print('Encerrado!')
        break
    else:
        qtd += 1
else:
    print('Dados Inseridos Com Sucesso!')
