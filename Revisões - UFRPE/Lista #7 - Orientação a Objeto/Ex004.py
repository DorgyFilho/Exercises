#004 - Modelar Uma Pessoa

class Pessoa():

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def emagrecer(self, dimPeso):
        self.peso -= dimPeso

    def engordar(self, incPeso):
        self.peso += incPeso
    
    def crescer(self, hei):
        self.altura += hei
    
    def envelhecer(self, age):
        if self.idade < 21:
            self.altura += (0.5/100)
        self.idade += 1
    
    def __repr__(self):
        return 'Nome: %s\nIdade: %d anos\nPeso: %d Kg\nAltura: %.2f m' %(self.nome, self.idade, self.peso, self.altura)

    
