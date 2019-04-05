#050 - Par Ou Ímpar

lista = []
N = int(input(''))
for i in range(N):
    lista.append(int(input('')))

for i in lista:
    if i % 2 == 0 and i > 0:
        print('EVEN POSITIVE')
    elif i % 2 == 0 and i < 0:
        print('EVEN NEGATIVE')
    elif i == 0:
        print('NULL')
    elif i % 2 != 0 and i > 0:
        print('ODD POSITIVE')
    elif i % 2 != 0 and i < 0:
        print('ODD NEGATIVE')