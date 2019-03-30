#121 - Parcela e Juros

divida = float(input('Digite o valor da dívida: '))
qtdParcelas = int(input('Digite o número de Parcelas: '))

for i in range(1,qtdParcelas+1):
    valorParcela = divida/i
    if 0 < i < 3:
        juros = 0
        parcela = valorParcela
        novaDivida = divida
    elif 3 <= i < 6:
        juros = (10/100)*divida
        parcela = valorParcela + juros
        novaDivida = divida + parcela
    elif 6 <= i < 9:
        juros = (15/100)*divida
        parcela = valorParcela + juros
        novaDivida = divida + parcela 
    elif 9 <= i < 12:
        juros = (20/100)*divida
        parcela = valorParcela + juros
        novaDivida = divida + parcela
    else:
        juros = (25/100)*divida
        parcela = valorParcela + juros
        novaDivida = divida + juros

    print(f'Valor da Dívida: R${divida:.2f} ---> Parcelas: {i} ---> Valor dos Juros: R${juros:.2f} ---> Parcela: R${parcela:.2f} ---> Novo Total: R${novaDivida:.2f}')