#076 - Fábrica
#10 Representantes
#Comissão para cada um conforme o número de pedidos.

for i in range(1,11):
    qtd = int(input('Quantidade de itens vendidos: '))
    if qtd < 20:
        print('Comissão 10%')
    elif 20 <= qtd < 50:
        print('Comissão 15%')
    elif 50 <= qtd < 75:
        print('Comissão 20%')
    elif qtd >= 75:
        print('Comissão 25%')
