#009 - Loja de Tintas

metros = int(input('Metros a serem pintados: '))
lts = metros/3

precoLata = 80
capLata = 18

qtdLata = lts/capLata
qtdLata = round(qtdLata)
totalCompra = qtdLata*precoLata

print(f'Quantidade de latas adquiridas: {qtdLata}\nValor total da compra: R${totalCompra:.2f}')
