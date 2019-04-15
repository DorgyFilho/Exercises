#168 - Nome na Vertical em Escada

nome = input('Nome: ').upper()
tam = len(nome)

for i in range(len(nome)):
    espaco = int(tam-i)//2
    novaString = ''*espaco+nome[:i+1]
    print(novaString)