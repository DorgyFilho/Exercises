#012 - Transformar a idade em dias.
anos = int(input('Anos Completos: '))
meses = int(input('Meses Completos: '))
dias = int(input('Dias Completos: '))
idadeDias = (meses*30) + (anos*365) + dias

print(f'Você tem {idadeDias} dias de idade.')
