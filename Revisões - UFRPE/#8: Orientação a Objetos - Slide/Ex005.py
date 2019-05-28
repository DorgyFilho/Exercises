#005 - Carro

class Carro():

    def __init__(self, consumo):
        self.consumo = consumo
        self.Gas = 0

    def addGas(self, qtdeGas):
        self.Gas += qtdeGas
    
    def andar(self, dist):
        distPercorrida = 0
        while True:
            combGasto = 1/self.consumo
            if combGasto <= self.Gas:
                self.Gas -= combGasto
            else:
                break
            distPercorrida += 1
            if distPercorrida == dist:
                break
        if distPercorrida == dist:
            return ('O carro andou %d Km' %dist)
        else:
            return ('O carro andou %d Km, mas o carro não possui combustível o bastante para concluir a viagem.' %dist)

    def getGas(self):
        return ('%.2f Litros' %self.Gas)

# MeuComb = int(input('Consumo do Carro Por Litro, em Km: '))
# MeuCarro = Carro(MeuComb)
# print(MeuCarro.getGas())
# print()
# Add = int(input('Quantidade de combustível a ser adicionada: '))
# MeuCarro.addGas(Add)
# print(MeuCarro.getGas())
# print()
# Dist = int(input('Distância Percorrida: '))
# print(MeuCarro.andar(Dist))
# print(MeuCarro.getGas())
# print()
# NovaDist = int(input('Nova Distância: '))
# print(MeuCarro.andar(NovaDist))
# print(MeuCarro.getGas())
