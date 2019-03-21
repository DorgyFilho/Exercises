#009 - Loja de Tintas

metros = int(input('Metros a serem pintados: '))
lts = metros//3

precoLata = 80
capLata = 18

qtdLata = lts//capLata
resto = lts % 18
if resto > 0:
    qtdLata += 1
totalCompra = qtdLata*precoLata

print(f'Quantidade de latas adquiridas: {qtdLata}\nValor total da compra: R${totalCompra:.2f}')


