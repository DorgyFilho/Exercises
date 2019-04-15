#169 - Nome na Vertical em Escada Invertida

nome = input('Nome: ')
tam = len(nome)

for j in range(len(nome), -1, -1):
    espaco = int(tam-j)//2
    nString = ''*espaco+nome[:j]
    print(nString)