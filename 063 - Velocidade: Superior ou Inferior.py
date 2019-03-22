#063 - Velocidade inferior ou superior à 110 Km/h

dist = int(input('Distância: '))
duraViagem = float(input('Tempo em horas: '))
vMedia = dist/duraViagem
if vMedia > 110:
    print(f'Velocidade: {vMedia:.0f} Km/h --> A velocidade foi superior a 110 Km/h')
elif vMedia == 110:
    print('Você está no limite de velocidade.')
else:
    print('A sua velocidade ficou abaixo dos 110 Km/h.')
