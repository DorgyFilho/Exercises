#025 - Lanche

linha = input().split(' ')

cod = int(linha[0])
qtd = int(linha[1])

if cod == 1:
    valor = qtd*4
elif cod == 2:
    valor = qtd*4.50
elif cod == 3:
    valor = qtd*5
elif cod == 4:
    valor = qtd*2
elif cod == 5:
    valor = qtd*1

print('Total: R$ %.2f' %valor)