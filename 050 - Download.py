#050 - Taxa de Download v2

#1 - Entrada de Dados
tam = float(input('Tamanho do arquivo em MB: '))
vel = float(input('Tamanho da velocidade em MBit: '))

#2 - Transformação de MB para Bits
tamBits = tam*1024*1024*8
tempoSec = tamBits / (vel*1024*1024)
tempoMin = tempoSec/60

#3 - Exiba o tempo em minutos
print(f'Tempo Estimado de Download: {round(tempoMin)} minutos.')


