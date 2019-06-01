#012 - Matriz

class Matriz():

    def __init__(self, l, c):
        self.__lin = l
        self.__col = c
        self.__M = {}
        self.iniciarM()
    
    def iniciarM(self):
        for m in range(self.__lin):
            for n in range(self.__col):
                self.__M[(m,n)] = 0
    
    def addNum(self, pLin, pCol, N):
        if pLin < self.__lin and pCol < self.__col:
            self.__M[(pLin, pCol)] = N
        else:
            print('Posição indisponível!')
    
    def __repr__(self):
        result = ''
        for m in range(self.__lin):
            for n in range(self.__col):
                result += ' ' + str(self.__M[(m,n)])
            result += '\n'
        return result

MATRIZ = Matriz(2,3)
MATRIZ.addNum(1,2,10)
print(MATRIZ)

