#013 - Matriz Transposta

class Matriz():

    def __init__(self, l, c):
        self.lin = l
        self.col = c
        self.M = {}
        # self.iniciarM()
        for m in range(self.lin):
            for n in range(self.col):
                self.M[(m,n)] = 0
    
    # def iniciarM(self):
    #     for m in range(self.__lin):
    #         for n in range(self.__col):
    #             self.M[(m,n)] = 0
    
    def addNum(self, pLin, pCol, N):
        if pLin < self.lin and pCol < self.col:
            self.M[(pLin, pCol)] = N
        else:
            print('Posição indisponível!')
    
    def __repr__(self):
        result = ''
        for m in range(self.lin):
            for n in range(self.col):
                result += ' ' + str(self.M[(n,m)])
            result += '\n'
        return result

MATRIZ = Matriz(3,3)
MATRIZ.addNum(1,2,10)
print(MATRIZ)