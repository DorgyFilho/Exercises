#007 - Turno Em Que a Pessoa Estuda

turno = input('Digite o turno - M/m - Matutino, V/v - Vespertino ou N/n - Noturno: ')
if turno == 'M' or turno == 'm':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite!')
else:
    print('Inválido!')