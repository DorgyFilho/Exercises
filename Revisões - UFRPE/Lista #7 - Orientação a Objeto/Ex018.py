#018 - Questão Extra 1:  Bola

class Bola:

    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.circ = circ
        self.mat = mat
    
    def trocaCor(self, novaCor):
        self.cor = novaCor
    
    def mostraCor(self):
        return self.cor

ball = Bola('Preto', 20, 'Metal')
print(ball.mostraCor())
print()
ball.trocaCor('Branco')
print(ball.mostraCor())