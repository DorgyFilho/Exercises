#020 - Idade Em Dias

dia = int(input(''))

ano = int(dia/365)
dia -= ano*365

mes = int(dia/30)
dia -= mes*30

print(repr(ano) + ' ano(s)')
print(repr(mes) + ' mes(es)')
print(repr(dia) + ' dia(s)')

