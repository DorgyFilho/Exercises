#003 - Bomba de Combustível

# class Bomba():

#     def __init__(self, tipo, valor, qtd):
#         self.tipo = tipo
#         self.valorLts = valor
#         self.qtdeComb = qtd
    
#     def addPorValor(self, valorReais):
#         litros = valorReais/self.valorLts
#         if litros > 0:
#             self.qtdeComb -= litros
#             return litros
#         else:
#             return 0

#     def addPorLitro(self, litros):
#         if litros > 0:
#             valor = litros*self.valorLts
#             self.qtdeComb -= litros
#             return valor
#         else:
#             return 0

#     def alteraPreco(self, novo):
#         if novo > 0:
#             self.valorLts = novo
#             return True
#         else:
#             return False
    
#     def alteraComb(self, Comb):
#         self.tipo = Comb
#         return True
    
#     def recarregar(self, Qtd):
#         self.qtdeComb += Qtd
#         return self.qtdeComb

class Bomba():

    tipoComb = None
    valorLts = None
    qtdeComb = None

    def __init__(self, tipo, preco, qtde):
        self.tipoComb = tipo
        self.valorLts = preco
        self.qtdeComb = qtde
    
    def addPorValor(self, Reais):
        litros = Reais/self.valorLts
        if litros > 0:
            self.qtdeComb -= litros
            return litros
        else:
            return 0

    
    def addPorLitro(self, Litros):
        if Litros > 0:
            valor = Litros*self.valorLts
            self.qtdeComb -= Litros
            return valor
        else:
            return 0

    def alterarPreco(self, novo):
        if novo > 0:
            self.valorLts = novo
            return True
        else:
            return False
    
    def alterarTipo(self, novoTipo):
        self.tipo = novoTipo
        return True
    
    def alterarBomba(self, Qtd):
        self.qtdeComb += Qtd
        return self.qtdeComb

Cliente = Bomba('G', 3.20, 1000)
print(Cliente.addPorLitro(50))
print(Cliente.qtdeComb)
print(Cliente.addPorValor(100))
print(Cliente.qtdeComb)



