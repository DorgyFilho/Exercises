#071 - Tipo de Combustível

opcao = int(input())  
A = 0
D = 0
G = 0
while opcao != 4:        
    if opcao == 1:
        A += 1
    elif opcao == 2:
        G += 1
    elif opcao == 3:
        D += 1
    opcao = int(input())

print('MUITO OBRIGADO')
print('Alcool: %d' %A)
print('Gasolina: %d' %G)
print('Diesel: %d' %D)
