#008 - Comissão

for i in range(1, 11):
    qtd = int(input('Quantidade de Produtos Vendidos: '))
    if qtd < 20:
        print('Comissão de 10%')
    elif qtd >= 20 and qtd < 50:
        print('Comissão de 15%')
    elif qtd >= 50 and qtd < 75:
        print('Comissão de 20%')
    else:
        print('Comissão de 25%')