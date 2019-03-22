#060 - Turno de Estudo

turno = input('Turno em que você estuda - M:Matutino, V:Vespertino ou N:Noturno: ').upper()
if turno == 'M':
    print('Matutino (Manhã)')
elif turno == 'V':
    print('Vespertino (Tarde)')
elif turno == 'N':
    print('Noturno (Noite)') 
else:
    print('Inválido!')