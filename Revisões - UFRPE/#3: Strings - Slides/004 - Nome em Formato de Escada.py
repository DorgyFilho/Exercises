#004 - Nome Em Formato de Escada

nome = input('Seu Nome: ').upper()
tam = len(nome)

for i in range(len(nome)):
    espaco = int(tam-i/2)
    escada = ""*espaco+nome[:i+1]
    print(f'{escada}')