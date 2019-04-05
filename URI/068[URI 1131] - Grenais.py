#068 - Grenais

resp = 1
grenais = 0
intWin = 0
greWin = 0
empate = 0
while resp == 1:
    gols = input().split(' ')
    i = int(gols[0])
    g = int(gols[1])
    if i > g:
        intWin += 1
    elif g > i:
        greWin += 1
    elif i == g:
        empate += 1
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())
print('%d grenais' %grenais)
print('Inter:%d' %intWin)
print('Gremio:%d' %greWin)
print('Empates:%d' %empate)
if intWin > greWin:
    print('Inter venceu mais')
elif greWin > intWin:
    print('Gremio venceu mais')
elif intWin == greWin:
    print('Nao houve vencedor')
