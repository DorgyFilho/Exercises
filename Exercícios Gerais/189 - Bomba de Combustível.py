#189 - Bomba de Combustível

class Bomba:

    def __init__(self, tipo):
        self.T = tipo
        self.P = 3.00
        self.C = 1000
    
    def tipoCombustivel(self, comb):
        self.T = comb
    
    def pegaTipo(self):
        return self.T
    
    def addPorValor(self, lts):
        if lts > 0:
            litros = lts//self.P
            self.C -= litros
            return 'Quantidade de litros abastecida: %d Litros' %litros
        else:
            return 'Valor Inválido!'

    def addPorLitro(self, litro):
        if litro > 0:
            valor = litro*self.P
            self.C -= litro
            return ('Valor a pagar: R$%.2f' %valor)
        else:
            return 'Valor inválido!'
    
    def recarregarBomba(self, novo):
        self.C += novo
    
    def mostraBomba(self):
        return '%d litros restantes no tanque.' %self.C

T = input('Tipo de Combustível: ')
Lamborghini = Bomba(T)
print(Lamborghini.mostraBomba())
print(Lamborghini.pegaTipo())
print(Lamborghini.addPorValor(40))
print(Lamborghini.mostraBomba())
print(Lamborghini.addPorLitro(60))
print(Lamborghini.mostraBomba())
Lamborghini.recarregarBomba(73)
print(Lamborghini.mostraBomba())

        
