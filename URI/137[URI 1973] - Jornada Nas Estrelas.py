#137 - Jornada Nas Estrelas

def inicio():
    N = int(input()) #Número de Estrelas
    K = [int(k) for k in input().split()]
    Total = sum(K)
    Att = [0]*N
    i = 0

    while i >= 0 and i < N:
        road = K[i] % 2
        if K[i] > 0:
            K[i] -= 1
            Att[i] = 1
            Total -= 1
        if road:
            i += 1
        else:
            i -= 1

    Att = Att.count(1)
    print(Att, Total)

inicio()