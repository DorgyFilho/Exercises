#023 - Exercício Extra 023: Carro

class Carro:

    def __init__(self, con):
        self.consumo = con
        self.Gas = 0
    
    def addGas(self, novo):
        self.Gas += novo
    
    def mostraGas(self):
        return self.Gas
    
    def andar(self, D):
        dist = 0
        while True:
            gasGasto = 1/self.Gas
            if gasGasto <= self.Gas:
                self.Gas -= gasGasto
            else:
                break
            dist += 1
            if dist == D:
                break
        if dist == D:
            return 'O carro andou %d Km' %D
        else:
            return 'O carro percorreu %d Km, mas a quantidade de combustível não foi o suficiente para completar a viagem.' %D

Consumo = Carro(10)
print(Consumo.mostraGas())
print()
Consumo.addGas(50)
print(Consumo.mostraGas())
print()
print(Consumo.andar(1560))