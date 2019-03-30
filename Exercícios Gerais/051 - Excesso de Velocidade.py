#051 - Excesso de Velocidade
#A cada 5 km excedidos, um ponto na carteira.
#Se ultrapassar 10 pontos, a carteira será suspensa.
altaVel = ''
excesso = ''
pontos = 0
vMax = 50
vel = int(input('Digite a sua velocidade: '))
if vel <= vMax:
    print('Você está livre!')
elif vel > vMax:
    altaVel = vel
    excesso = altaVel - 50
    for spd in range(1, excesso+1):
        if spd % 5 == 0:
            pontos += 1
    print(f'Você tem {pontos} pontos na carteira')
    if pontos > 10:
        print('A sua carteira foi suspensa')


