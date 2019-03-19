#015 - Tempo do Jogo

hStart = int(input('Hora Inicial: '))
mStart = int(input('Minuto Inicial: '))
hEnd = int(input('Hora Final: '))
mEnd = int(input('Minuto Final: '))

mtStart = (hStart*60) + mStart
mtEnd = (hEnd*60) + mEnd

if hStart > hEnd:
    mtEnd += (24*60)

duracao = mtEnd - mtStart
hora = duracao/60
if type(hora) == float:
    hora = int(hora)
min = duracao%60

print(f'{hora}:{min}')