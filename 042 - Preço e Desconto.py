#042 - Valor de uma mercadoria

preco = float(input('Preço de uma mercadoria: '))
percDesc = int(input('Desconto a ser condedido: '))
desconto = (percDesc/100)*preco
novoPreco = preco - desconto
print(f'Preço Original: R${preco:.2f}\nDesconto Concedido: R${desconto:.2f}\nNovo Preço: R${novoPreco:.2f}')
