#018 - Aluguel do Carro

mod = input('Modelo do Carro: ').upper()
ano = int(input('Ano do Veículo (Ex: 2015): '))
placa = input('Placa do Carro (Ex: ABC-1234): ').upper()
pSugerido = int(input('Preço Sugerido do Aluguel: R$'))

if mod == 'FERRARI':
    taxaFer = (20/100)*pSugerido
    if ano > 2015:
        taxaInc = (20/100)*pSugerido
        pFerrari = pSugerido + taxaInc + taxaFer
    elif 2000 <= ano < 2015:
        pFerrari = pSugerido + taxaFer
    else:
        taxaDecFer = (20/100)*pSugerido
        pFerrari = pSugerido - taxaDecFer + taxaFer
    print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nValor: R${pFerrari:.2f}')

elif ano > 2015:
    taxaInc = (20/100)*pSugerido
    nPreco = pSugerido + taxaInc
    print(f'Mod: {mod}\nAno: {ano}\nPlaca: {placa}\nValor: R${nPreco:.2f}')

elif 2000 <= ano < 2015:
    print(f'Mod: {mod}\nAno: {ano}\nPlaca: {placa}\nValor: R${pSugerido:.2f}')

elif ano < 2000:
    taxaDec = (20/100)*pSugerido
    nPreco = pSugerido - taxaDec
    print(f'Mod: {mod}\nAno: {ano}\nPlaca: {placa}\nValor: R${nPreco:.2f}')

