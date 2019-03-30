#039 - Tempo de Download

#1 - Taxa de Transferência
#1Mbit - 1024 bytes
Mega = int(input('Tamanho do Arquivo em MB: '))
MultiMB = Mega*1024
KB = MultiMB/8 #1 byte tem 8 bits
VelTransf = KB

#2 - Tempo de Download
M = Mega*1024
taxaTransf = M/VelTransf #Segundos
tempo = taxaTransf/60 #Minutos

print(f'Velocidade: {VelTransf:.2f} KB/s ---> Tempo Estimado: {tempo:.2f} minutos')