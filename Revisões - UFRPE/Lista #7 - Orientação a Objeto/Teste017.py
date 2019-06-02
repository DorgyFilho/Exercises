#017 - Teste017

from Ex017 import *

Cadastros = Gerencial()
Dorgival = Cadastros.cadastrarFunc()
Cecilia = Vendedor('Cecilia', 'Vendedora', 3000, '4321', 12000, 15000)
L1 = Loja(123, 30000, Dorgival)
L1.addVendedor(Cecilia)
print('Total de Vendas: %.2f' %L1.obterTotalVendas())