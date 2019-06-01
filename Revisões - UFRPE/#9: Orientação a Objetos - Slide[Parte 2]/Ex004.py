#004 - Ponto

class Ponto():

    def __init__(self):
        self.__Pontos = []
    
    def addPontos(self, novo):
        self.__Pontos.append(novo)
    
    def imprimirLista(self):
        for ponto in self.__Pontos:
            print(ponto, end='')

Texto = open('/home/dorgival/pontos.txt')
Lista = Texto.read()
Texto.close()
for prod in Lista:
    K = Ponto()
    K.addPontos(prod)
    K.imprimirLista()