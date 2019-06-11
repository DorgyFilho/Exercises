#201 - Compras

class Produto:

    def __init__(self, cod = 0, peso = 0, dim = 0, preco = 0):
        self.cod = cod
        self.peso = peso
        self.dim = dim
        self.preco = preco
    
class Carrinho:

    def __init__(self):
        self.Carrinho = []
        self.Total = 0
    
    def addProduto(self, resp):
        self.Carrinho.append(resp)
        print('Produto adicionado.')

    def removerProduto(self, Prod):
        self.Carrinho.remove(Prod)

    def calcularTotal(self, resp):
        self.Total = resp
        print('Total do carrinho: %.2f' %(self.Total))

Total = 0
while True:
    prod = input().lower().replace('\n','').replace('\r','')
    if prod == 'fim':
        break
    else:
        if 'add' in prod: 
            Carro = prod.split(':')[1:]  
            P = Produto(Carro[0], Carro[1], Carro[2], Carro[3]) 
            C = Carrinho()      
            C.addProduto(P)
            Valor = float(Carro[3])
            Frete = (float(Carro[1])*float(Carro[2]))*2.00
            Total = Total + Valor + Frete
        if prod == 'clear':
            C.removerProduto(P)
            Total=0
        if prod == 'total':
            C.calcularTotal(Total)


