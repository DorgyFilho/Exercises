#152 - Batalha de Pomekons

qtd = int(input())
Hit = 0
Hit2 = 0
for i in range(1, qtd+1):
    bonus = int(input())
    Att, Def, Level = map(int, input().split())
    A, D, L = map(int, input().split())
    
    if Level % 2 == 0:
        Hit = ((Att + Def)/2) + bonus
    else:
        Hit = ((Att + Def)/2)
    
    if L % 2 == 0:
        Hit2 = ((A+D)/2) + bonus
    else:
        Hit2 = ((A+D)/2)
    
    if Hit < Hit2:
        print('Guarte')

    elif Hit > Hit2:
        print('Dabriel')

    else:
        print('Empate')



