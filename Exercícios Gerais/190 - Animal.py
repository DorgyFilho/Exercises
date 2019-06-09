#190 - Animal

class Animal:

    def __init__(self, nomeEspecie, qtd = 0):
        self.Especie = nomeEspecie
        self.Quantidade = qtd
    
    def addAnimal(self, novo):
        self.Especie = novo
    
    def pegaAnimal(self):
        return self.Especie
    
    def addQtd(self, qtde):
        self.Quantidade += qtde
    
    def pegaQtde(self):
        return self.Quantidade

Nome = input('Nome do animal: ')
Qtde = int(input('Quantidade: '))
Novo = Animal(Nome, Qtde)
print(Novo.pegaAnimal())
print(Novo.pegaQtde())