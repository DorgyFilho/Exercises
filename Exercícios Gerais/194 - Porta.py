#194 - Porta

class Porta:

    def __init__(self, cor, X, Y, Z):
        self.cor = cor
        self.X = X
        self.Y = Y
        self.Z = Z
        self.aberta = True
    
    def abrePorta(self, num):
        if num == 1:
            self.aberta = True
        else:
            self.aberta = False
    
    def estaAberta(self):
        return self.aberta

    def pintar(self, novaCor):
        self.cor = novaCor
    
    def corPorta(self):
        return self.cor
    
Door = Porta('Preto', 2.10, 0.50, 1.85)
Door.abrePorta(0)
print(Door.estaAberta())
print(Door.corPorta())