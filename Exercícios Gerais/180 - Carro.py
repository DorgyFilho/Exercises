#180 - Carro

class Carro():

    def __init__(self, consumo):
        self.con = consumo
        self.tanque = 0

    def addGas(self, novo):
        self.tanque = novo
    
    def mostraGas(self):
        return 'Quantidade atual de combustível: %d Litros' %self.tanque
    
    def andar(self, dist):
        gasto = dist/self.tanque
        if self.tanque < gasto:
            print('A quantidade de combustível não é a suficiente para completar a viagem.')
            print(self.mostraGas())
        else:
            self.tanque -= gasto
            print('A quantidade de combustível é o suficiente para completar a viagem!')
            print(self.mostraGas())

Gol = Carro(10)
print(Gol.mostraGas())
print()
Gol.addGas(50)
print(Gol.mostraGas())
print()
Gol.andar(2500)
print()
