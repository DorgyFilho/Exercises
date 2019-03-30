#135 - Caixa [Valor a Pagar]

pgto = float(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
pagar = pgto

while True:
    if atual <= pagar:
        pagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print(f'{cedulas} cedulas de R${atual}')
        else:
            print(f'{cedulas} moedas de R${atual}')
        if pagar < 0.01:
            print('Valores menores que 0.01 não são aceitos.')
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0
