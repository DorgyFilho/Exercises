#023 - Experimento de Física

tempo = 0
VI = float(input('Velocidade Inicial em m/s: '))
AG = 10

while True:
    VF = VI - (AG*tempo)
    print(f'Tempo: {tempo} ---- Velocidade: {VF} m/s')
    tempo += 1
    if VF == 0:
        break