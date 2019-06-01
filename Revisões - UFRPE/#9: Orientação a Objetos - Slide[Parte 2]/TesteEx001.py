#001 - Teste Ex001

from Ex001 import *

codigo = int(input('Código do produto: '))
preco = float(input('Preço do produto: '))
Prod = Produto(codigo, preco)
Prod2 = Produto(2, 100)
print(Prod)
print(Prod2)
print(Prod.qtdProd)