#117 - A Corrida de Lesmas

while True:
    V = []
    try:
        spd = int(input())
    except EOFError:
        break

    Vel = input()
    V = Vel.split()

    for k in range(len(V)):
        V[k] = int(V[k])
    
    if max(V) < 10:
        print('1')
    elif 10 <= max(V) < 20:
        print('2')
    elif max(V) >= 20:
        print('3')