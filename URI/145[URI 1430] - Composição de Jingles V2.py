Notas = {'W':1,'H':1/2,'Q':1/4,'E':1/8,'S':1/16,'T':1/32,'X':1/64}

while True:
    melodia = input().strip()
    if melodia == '*':
        break
    melodia = melodia.split('/')
    musica = []
    for C in melodia:
        musica.append(C)
    total = 0
    for rock in musica:
        tempo = 0
        for metal in rock:
            tempo += Notas[metal]
            if tempo > 1: 
                break
        if tempo == 1: 
            total += 1
    print(total)

        


