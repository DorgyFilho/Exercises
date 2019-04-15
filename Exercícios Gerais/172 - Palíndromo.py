#172 - Palíndromo

frase = input('Frase: ').upper()
novaFrase = frase.split()
uniao = ''.join(novaFrase)
inverso = ''

for i in range(len(uniao)-1, -1, -1):
    inverso += uniao[i]
print()
print(f'{uniao} ---> {inverso}')
print()
if inverso == uniao:
    print('É Palíndromo!')
else:
    print('Não é Palíndromo!')