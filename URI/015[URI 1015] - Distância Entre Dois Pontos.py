#015 - Distância Entre Dois Pontos

X = input().split(' ')
Y = input().split(' ')

x1, y1 = X
x2, y2 = Y
x = (float(x2) - float(x1))**2
y = (float(y2) - float(y1))**2
dist = (x + y)**0.5

print('%.4f' %dist)
