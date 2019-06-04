#003 - Bomba de Combustível

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



