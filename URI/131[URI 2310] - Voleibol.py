#131 - Voleibol

Players = int(input())
ST = []
BT = []
AT = []
SC = []
BC = []
AC = []

for player in range(Players):
    nome = input()
    S, B, A = map(int, input().split())
    ST.append(S)
    BT.append(B)
    AT.append(A)
    S1, B1, A1 = map(int, input().split())
    SC.append(S1)
    BC.append(B1)
    AC.append(A1)

print('Pontos de Saque: {:.2f} %.'.format((sum(SC)/sum(ST))*100))
print('Pontos de Bloqueio: {:.2f} %.'.format((sum(BC)/sum(BT))*100))
print('Pontos de Ataque: {:.2f} %.'.format((sum(AC)/sum(AT))*100)) 
