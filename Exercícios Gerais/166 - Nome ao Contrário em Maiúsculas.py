#166 - Nome ao Contrário em Maiúsculas

nome = input('Nome: ').upper()
pos = len(nome)-1
nomeInv = ''

while pos >= 0:
    nomeInv += nome[pos]
    pos -= 1
print(f'{nome} ---> {nomeInv}')
