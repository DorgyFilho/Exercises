#109 - Loja do Sr. Manoel

preco = 1.99

qtdProd = int(input('Quantidade de Produtos Adquirida: '))

print('Loja Quase Dois ---- Tabela de Preços')
for i in range(1, qtdProd+1):
    valor = preco*i
    print(f'{i} ----> Valor: R${valor:.2f}')