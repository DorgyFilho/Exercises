#002 - Gerenciador de Produtos

from Ex001 import Produto

class GerProd():

    def __init__(self):
        self.__listaProd = []
    
    def addProd(self, novo):
        self.__listaProd.append(novo)
    
    def removerProd(self, cod):
        removido = 0
        for prod in self.__listaProd:
            if prod.getProd() == cod:
                break
            removido += 1
        self.__listaProd.pop(removido)

    def imprimirProd(self):
        for prod in self.__listaProd:
            print(prod)

gProd = GerProd()
Biscoito = Produto(1, 2.50)
Macarrao = Produto(2, 1.20)
Suco = Produto(3, 1.80)
gProd.addProd(Biscoito)
gProd.addProd(Macarrao)
gProd.addProd(Suco)
gProd.removerProd(1)
gProd.imprimirProd()