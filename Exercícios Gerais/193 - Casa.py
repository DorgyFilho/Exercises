#193 - Casa

class Casa:
    #True: Aberto e False: Fechado
    def __init__(self, cor):
        self.cor = cor
        self.__porta1 = 0
        self.__porta2 = 0
        self.__porta3 = 0
        self.soma = 0
    
    def defineCor(self, novo):
        self.cor = novo
    
    def pegaCor(self):
        return self.cor
    
    def abreTudo(self):
        self.soma = self.__porta1 + self.__porta2 + self.__porta3
        while self.soma < 3:
            self.soma += 1
        return True
    
    def fechaTudo(self):
        self.soma = self.__porta1 + self.__porta2 + self.__porta3
        while self.soma > 0:
            self.soma -= 1
        return False
    
    def qtdPortasAbertas(self):
        return 'Há %d porta(s) aberta(s)' %self.soma

Dorgival = Casa('Azul')
print(Dorgival.abreTudo())
print(Dorgival.qtdPortasAbertas())
print(Dorgival.fechaTudo())
print(Dorgival.qtdPortasAbertas())
    


    
