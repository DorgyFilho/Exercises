#003 - Velocidade Média: Superior ou Inferior à 110 Km/h.

dist = int(input('Digite a distância do percurso: '))
tempo = float(input('Digite o tempo em horas: '))
vMedia = dist/tempo
if vMedia > 110:
    print('Você está acima da velocidade média de 110 Km/h.')
elif vMedia == 110:
    print('A sua velocidade é igual à velocidade média de 110 Km/h.')
else:
    print('A sua velocidade está abaixo da velocidade média de 110 Km/h.')
    