#117 - Censo na Academia

maisGordo = 0
maisMagro = 1000
maisBaixo = 1000
maisAlto = 0
codAlto = 0
codBaixo = 0
codGordo = 0
codMagro = 0
somaPeso = 0
somaAltura = 0
mPeso = 0
mAltura = 0
qtdClientes = 0

while True:
    cod = int(input('Digite o seu código: '))
    if cod == 0:
        print('Programa Encerrado!')
        break
    qtdClientes += 1
    altura = float(input('Sua Altura: '))
    peso = float(input('Seu Peso: '))
    somaAltura += altura
    somaPeso += peso
    if altura > maisAlto:
        maisAlto = altura
        codAlto = cod
    if altura < maisBaixo:
        maisBaixo = altura
        codBaixo = cod
    if peso < maisMagro:
        maisMagro = peso
        codMagro = cod
    if peso > maisGordo:
        maisGordo = peso
        codGordo = cod

mAltura = somaAltura/qtdClientes
mPeso = somaPeso/qtdClientes

print(f'Mais Alto: {codAlto} ---> Altura: {maisAlto} m')
print(f'Mais Baixo: {codBaixo} ---> Altura: {maisBaixo} m')
print(f'Mais Magro: {codMagro} ---> Peso: {maisMagro} kg')
print(f'Mais Gordo: {codGordo} ---> Peso: {maisGordo} kg')
print(f'Soma do Peso: {somaPeso:.2f} kg')
print(f'Soma da Altura: {somaAltura:.2f} m')
print(f'Média do Peso: {mPeso:.2f} kg')
print(f'Média da Altura: {mAltura:.2f} m')
