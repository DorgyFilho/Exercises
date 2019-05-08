#142 - Domingo de Manhã

while True:
    try:
        horario = input().split(':')
        hora = int(horario[0])
        minuto = int(horario[1])
        Total = (hora*60) + minuto + 60
        if Total <= 480:
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: %d' %(Total-480))

    except EOFError:
        break
