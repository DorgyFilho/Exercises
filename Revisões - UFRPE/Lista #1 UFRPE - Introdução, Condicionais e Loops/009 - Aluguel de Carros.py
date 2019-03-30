#009 - Aluguel de Carros

repetir = 'S'
while repetir == 'S':
    mod = input('Modelo do Carro: ').upper()
    ano = int(input('Ano do Carro: '))
    placa = input('Placa do Carro: ').upper()
    pAluguel = float(input('Preço do Aluguel: R$ '))

    if mod == 'FERRARI':
        vIncFer = (20/100)*pAluguel
        if ano > 2015:
            vInc = (20/100)*pAluguel
            novoPreco = pAluguel + vInc + vIncFer
            print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${novoPreco:.2f}')
        elif ano >= 2000 and ano < 2015:
            novoPreco = pAluguel + vIncFer
            print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${novoPreco:.2f}')
        elif ano < 2000:
            vDec = (10/100)*pAluguel
            novoPreco = pAluguel - vDec + vIncFer
            print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${novoPreco:.2f}')
    elif ano > 2015:
        vInc = (20/100)*pAluguel
        novoPreco = pAluguel + vInc
        print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${novoPreco:.2f}')
    elif ano >= 2000 and ano < 2015:
        print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${pAluguel:.2f}')
    elif ano < 2000:
        vDec = (10/100)*pAluguel
        novoPreco = pAluguel - vDec
        print(f'Modelo: {mod}\nAno: {ano}\nPlaca: {placa}\nAluguel: R${novoPreco:.2f}')
    
    print()
    print('Deseja Repetir a Operação? S/N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado. Obrigado(a) e volte sempre!')
        break

else:
    print('Opção Inválida!')