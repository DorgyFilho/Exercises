#154 - Zodíaco Chinês

ano = int(input('Digite o ano: '))

if (ano - 2000) % 12 == 0:
    signo = 'Dragão'
elif (ano - 2000) % 12 == 1:
    signo = 'Cobra'
elif (ano - 2000) % 12 == 2:
    signo = 'Cavalo'
elif (ano - 2000) % 12 == 3:
    signo = 'Ovelha'
elif (ano - 2000) % 12 == 4:
    signo = 'Macaco'
elif (ano - 2000) % 12 == 5:
    signo = 'Galo'
elif (ano - 2000) % 12 == 6:
    signo = 'Cachorro'
elif (ano - 2000) % 12 == 7:
    signo = 'Porco'
elif (ano - 2000) % 12 == 8:
    signo = 'Rato'
elif (ano - 2000) % 12 == 9:
    signo = 'Touro'
elif (ano - 2000) % 12 == 10:
    signo = 'Tigre'
else:
    signo = 'Lebre'

print(f'Signo: {signo}')