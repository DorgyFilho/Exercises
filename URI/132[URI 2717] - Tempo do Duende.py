#Tempo do Duende

Tempo = int(input())
Valor = input().split()
A = int(Valor[0])
B = int(Valor[1])
Total = A + B
if Total > Tempo:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')