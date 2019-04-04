#033 - Tempo de Jogo Com Minutos

linha = input().split()
hIni = int(linha[0])
mIni = int(linha[1])
hFim = int(linha[2])
mFim = int(linha[3])

hT = hFim - hIni
mT = mFim - mIni

if hT < 0:
    hT += 24

if mT < 0:
    mT += 60
    hT -= 1

if mT == 0 and hT == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:   
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hT, mT))