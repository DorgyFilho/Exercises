#001 - Produto

class Produto():
    
    qtdProd = 0
    def __init__(self, cod, preco):
        self.__cod = cod
        self.__preco = preco
        Produto.qtdProd += 1
    
    def getProd(self):
        return self.__cod
    
    def getPreco(self):
        return self.__preco

    def setProd(self, novocod):
        if novocod >= 0:
            self.__cod = novocod
            self.qtdProd += 1
        else:
            self.__cod = 0
    
    def setPreco(self, novoPreco):
        if novoPreco >= 0:
            self.__preco = novoPreco
        else:
            self.__preco = 0

    def __repr__(self):
        return '%s -- R$%.2f'%(self.__cod, self.__preco)

# codigo = int(input('Código do produto: '))
# preco = float(input('Preço do produto: '))
# Prod = Produto(codigo, preco)
# Prod2 = Produto(2, 100)
# print(Prod)
# print(Prod2)
# print(Prod.qtdProd)