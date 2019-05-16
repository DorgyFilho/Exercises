#003 - Idade em Dias

anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

IdadeEmDias = (anos*365) + (meses*30) + dias

print(f'A sua idade em dias: {IdadeEmDias}')