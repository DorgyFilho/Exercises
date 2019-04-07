#006 - É Palíndromo?

frase = input('Frase: ').strip().upper()
novaFrase = frase.split()
uniao = "".join(novaFrase)
fInv = ''

for let in range(len(uniao)-1, -1, -1):
    fInv += uniao[let]
print(f'{uniao} ---> {fInv}')
print()
if fInv == uniao:
    print('Palindromo!')
else:
    print('Não é Palindromo!') 