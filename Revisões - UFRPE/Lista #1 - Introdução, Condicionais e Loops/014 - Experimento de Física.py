#014 - Experimeto de Física

vI = float(input('Velocidade: '))
t = 0
AG = 10.0

while True:
    vF = vI - (AG*t)
    print(f'Tempo = {t} ---> Velocidade: {vF} m/s')
    t += 1
    if vF == 0:
        break