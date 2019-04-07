#010 - Língua Inglesa
frase = input('Frase em inglês: ')
novaFrase = frase.split()
sujeito = novaFrase[0]
verbo = novaFrase[1]
verbInt = novaFrase[1]
compl1 = novaFrase[2]
compl2 = novaFrase[3]
neg = 'not'
ask = '?'

negativa = sujeito + ' ' + verbo + ' ' + neg + ' ' + compl1 + ' ' + compl2
interrogativa = verbInt + ' ' + sujeito + ' ' + compl1 + ' ' + compl2 + ask
fNeg = ''.join(negativa)
fInt = ''.join(interrogativa)
print(fNeg)
print(fInt)