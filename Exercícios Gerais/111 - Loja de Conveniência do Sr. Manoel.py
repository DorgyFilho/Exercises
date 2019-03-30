#111 - Loja de Conveniência do Sr. Manoel

repetir = 'S'
while repetir == 'S':
    print('Loja de Conveniência do Sr. Manoel')
    total = 0
    nProd = 1
    while True:
        preco = float(input('Informe o preço do produto: '))
        nProd += 1
        total += preco
        if preco == 0:
            break
    
    print()
    print('Loja de Conveniência do Sr. Manoel')
    print()
    print(f"Total: R${total:.2f}")
    print()
    pagar = float(input('Valor a Pagar: '))
    print()
    troco = pagar - total
    if pagar < total:
        print('Pague com o valor correto.')
    else:
        print(f'Troco: R${troco:.2f}')
    
    print()
    print('Deseja repetir a operação? - S ou N')
    print()
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Caixa Encerrado!')
        break
else:
    print('Opção Inválida!')

