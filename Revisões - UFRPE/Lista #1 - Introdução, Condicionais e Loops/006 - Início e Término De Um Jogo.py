#006 - Início e Término De Um Jogo

hIni = int(input('Hora Inicial: '))
mIni = int(input('Minuto Inicial: '))
hFim = int(input('Hora Final: '))
mFim = int(input('Minuto Final: '))

mtIni = (hIni*60) + mIni
mtFim = (hFim*60) + mFim

if hIni > hFim:
    mtFim += (24*60)

duracao = mtFim - mtIni
hora = duracao//60
minuto = duracao%60

print(f'{hora}:{minuto}')