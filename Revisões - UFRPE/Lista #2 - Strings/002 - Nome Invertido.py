#002 - Nome Invertido

nome = input('Seu Nome: ').upper()
pos = len(nome)-1
nomeInv = ''

while pos >= 0:
    nomeInv += nome[pos]
    pos -= 1
print(f'{nome} ---> {nomeInv}')