#043 - Tempo de uma viagem

distancia = int(input('Distância entre a origem e o destino: '))
vMedia = int(input('Velocidade Media em km/h: '))
tempo = distancia/vMedia
print(f'Tempo da viagem: {tempo} horas')

tSec = int(tempo*3600)
tHor = int(tSec/3600)
tSec = int(tHor%3600)
tMin = int(tSec/60)
Sec= int(tSec%60)

print(f'{tHor:02d}:{tMin:02d}:{Sec:02d}')