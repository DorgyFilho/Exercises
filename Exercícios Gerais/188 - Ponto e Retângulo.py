#188 - Ponto e Retângulo

class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostraPontos(self):
        print('x = %d, y = %d' %(self.x, self.y))

class Retangulo:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def centro(self):
        canX = ((self.X.x + self.Y.x)//2.0)
        canY = ((self.X.y + self.Y.y)//2.0)
        return (canX, canY)

x1 = int(input('X: '))
y1 = int(input('Y: '))
k1 = Ponto(x1,y1)
x2 = int(input('X: '))
y2 = int(input('Y: '))
k2 = Ponto(x2, y2)
Result = Retangulo(k1, k2)
k1.mostraPontos()
k2.mostraPontos()
print(Result.centro())