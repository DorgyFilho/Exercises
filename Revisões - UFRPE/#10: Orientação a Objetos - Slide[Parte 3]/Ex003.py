#003 - Atleta

class Atleta:

    def __init__(self, A, W):
        self.__A = A
        self.__W = W

    def aposentar(self):
        return 'Estou Aposentado.'
    
    def aquecer(self, P):
        self.__W = P

class Corredor(Atleta):

    def Correr(self, peso):
        self.aquecer(peso)
        print('Pratico Corrida!')

class Nadador(Atleta):
    
    def Nadar(self, peso):
        self.aquecer(peso)
        print('Pratico Natação!')
        # self.aposentar(resposta)
        # if self.aposentar(resposta) == False:
        #     self.aquecer(peso)
        # else:
        #     self.aposentar(resposta) = True

class Ciclista(Atleta):
    
    def Pedalar(self, peso):
        self.aquecer(peso)
        print('Pratico Ciclismo!')
        

class TriAtleta(Atleta):

    def Esportista(self):
        return 'Eu sou um esportista!'

A = input('Aposentado? S/N: ').upper()
W = float(input('Peso: '))
if A == 'N' and W >= 0:
    Dorgival = Corredor(A,W)
    Dorgival.Correr(W)
    Dorgival = Nadador(A,W)
    Dorgival.Nadar(W)
    Dorgival = Ciclista(A,W)
    Dorgival.Pedalar(W)
    Dorgival = TriAtleta(A, W)
    print(Dorgival.Esportista())
if A == 'S' and W >= 0:
    Dorgival = Atleta(A,W)
    print(Dorgival.aposentar())

