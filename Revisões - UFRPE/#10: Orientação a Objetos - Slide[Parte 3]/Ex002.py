#002 - Forma Geométrica

class Forma:

    def __init__(self):
        self.__A = 0
        self.__P = 0
    
    def definirP(self, p):
        self.__P = p
    
    def obterP(self):
        return self.__P
    
    def definirA(self, a):
        self.__A = a
    
    def obterA(self):
        return self.__A

class Ret(Forma):

    def __init__(self, L1, L2):
        Forma.__init__(self)
        self.__L1 = L1
        self.__L2 = L2
    
    def calculaP(self):
        self.definirP(2*self.__L1 + 2*self.__L2)
    
    def calculaA(self):
        self.definirA(self.__L1 * self.__L2)

class Tri(Forma):

    def __init__(self, L1, L2, L3, H):
        Forma.__init__(self)
        self.__L1 = L1
        self.__L2 = L2
        self.__L3 = L3
        self.__H = H
    
    def calculaP(self):
        self.definirP(self.__L1 + self.__L2 + self.__L3)
    
    def calculaA(self):
        self.definirA((self.__L1 * self.__H)/2)

R = Ret(8,5)
R.calculaP()
R.calculaA()
print('Resultado do Retângulo:')
print(R.obterP())
print(R.obterA())

print()
T = Tri(4,5,6,12)
T.calculaP()
T.calculaA()
print('Resultado do Triângulo:')
print(T.obterP())
print(T.obterA())