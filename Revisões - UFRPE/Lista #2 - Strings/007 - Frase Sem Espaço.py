#007 - Frase Sem Espaço

frase = input('Frase: ').strip()
novaFrase = frase.split()
nFrase = ''.join(novaFrase)
print(f'{nFrase}')