#123 - Lanchonete

pHDog = 1.20
pBauru = 1.30
pBauOvo = 1.50
pHamb = 1.20
pCheeseBur = 1.30
pRefri = 1.00
conta = 0

qtdeHDog = 0
qtdeBau = 0
qtdeBauOvo = 0
qtdeHamb = 0
qtdeCheese = 0
qtdeRefri = 0

totalConta = 0

codigo = ''

print('Lanches ---> Código ---> Preço')
print('='*30)
print('Cachorro Quente ---> 100 ---> R$1.20')
print('Bauru ---> 101 ---> R$1.30')
print('Bauru Com Ovo ---> 102 ---> R$1.50')
print('Hamburguer ---> 103 ---> R$1.20')
print('Chesseburguer ---> 104 ---> R$1.30')
print('Refrigerante ---> 105 ---> R$1.00')
print()

while True:
    pedido = int(input('Digite o código: '))
    if pedido < 100 or pedido > 105:
        print('Programa Encerrado!')
        break
    print()
    qtde = int(input('Quantidade deste pedido: '))
    if qtde < 1:
        print('Programa Encerrado!')
        break
    print()
    if pedido == 100:
        qtdeHDog += qtde
        conta = qtde*pHDog
        codigo = 'Cachorro Quente'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeHDog} --- Subtotal: R${conta:.2f}')
        print()
    elif pedido == 101:
        qtdeBau += qtde
        conta = qtde*pBauru
        codigo = 'Bauru'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeBau} --- Subtotal: R${conta:.2f}')
        print()  
    elif pedido == 102:
        qtdeBauOvo += qtde
        conta = qtde*pBauOvo
        codigo = 'Bauru Com Ovo'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeBauOvo} --- Subtotal: R${conta:.2f}')
        print()
    elif pedido == 103:
        qtdeHamb += qtde
        conta = qtde*pHamb
        codigo = 'Hamburguer'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeHamb} --- Subtotal: R${conta:.2f}')
        print()
    elif pedido == 104:
        qtdeCheese += qtde
        conta = qtde*pCheeseBur
        codigo = 'CheeseBurguer'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeCheese} --- Subtotal: R${conta:.2f}')
        print()
    elif pedido == 105:
        qtdeRefri += qtde
        conta = qtde*pRefri
        codigo = 'Refrigerante'
        print(f'Pedido: {codigo} --- Quantidade: {qtdeRefri} --- Subtotal: R${conta:.2f}')    
        print()   
    totalConta += conta

print()
print(f'Total a Pagar: R${totalConta:.2f}')
    


    