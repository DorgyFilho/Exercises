#003 - Verificar IP

arq = open(input('Arquivo: '))
IPs = arq.readlines()
arq.close()

for i in range(len(IPs)):
    End = IPs[i].split('.')
    if int(End[0]) <= 254 and int(End[1]) <= 254 and int(End[2]) <= 254 and int(End[3]) <= 254:
        print(f'Válido - {IPs[i]}')
    else:
        print(f'Inválido - {IPs[i]}')