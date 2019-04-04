#032 - Tempo de Jogo

linha = input().split()

hIni = int(linha[0])
hFim = int(linha[1])

if hIni > hFim:
    Extra = 24 - hIni
    hora = Extra + hFim
    print('O JOGO DUROU %d HORA(S)' %hora)

elif hFim > hIni:
    hora = hFim - hIni
    print('O JOGO DUROU %d HORA(S)' %hora)

elif hIni == hFim:
    hora = 24
    print('O JOGO DUROU %d HORA(S)' %hora)


