#171 - Identificando o Chá

TeaFlavour = int(input())
a,b,c,d,e = map(int, input().split())
Players = a,b,c,d,e

Acertos = 0
for i in range(len(Players)):
    if Players[i] == TeaFlavour:
        Acertos += 1
print(Acertos)  