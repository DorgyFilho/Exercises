#192 - Restaurante

class Restaurante:

    def __init__(self, nome, tipo):
        self.nome = nome
        self.cozinha = tipo
    
    def addNome(self, novo):
        self.nome = novo
    
    def addCozinha(self, novo):
        self.cozinha = novo
    
    def pegaNome(self):
        return self.nome
    
    def pegaCozinha(self):
        return self.cozinha

nome = input('Nome do restaurante: ')
tipo = input('Ramo da gastronomia: ')
Estabelecimento = Restaurante(nome, tipo)
print('Nome: %s, Tipo: %s' %(Estabelecimento.pegaNome(), Estabelecimento.pegaCozinha()))