#009 - Taxonomia

class Animal():

    def __init__(self, comum, cient):
        self.comum = comum
        self.cient = cient
    
    def validoLatim(self, Nome):
        Nome = self.cient.split()
        if Nome[0][0].isupper() and Nome[1][0].islower():
            return 'Nome Válido!'
        else:
            return 'Nome Inválido!'
    
    def Genero(self, Gen):
        Gen = self.cient.split()
        return Gen[0]
    
    def Especie(self, Esp):
        Esp = self.cient.split()
        return Esp[1]

# # comum = input('Nome Comum: ')
# # latim = input('Nome em latim: ')   
# comum = 'Papagaio-Verdadeiro'
# latim = 'Amazona aestiva'
# Lista = latim.split()
# Resultado = Animal('Papagaio-Verdadeiro', 'Amazona aestiva')
# print(Resultado.validoLatim(latim))
# print(Resultado.Genero(Lista[0]))
# print(Resultado.Especie(Lista[1]))