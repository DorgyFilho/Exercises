#176 - Correção de Telefone

print('Valida e Corrije o número de telefone.')
telefone = input('Digite o telefone: ')
tam = len(telefone)

if telefone.isdigit() and tam == 7:
    print('Telefone possui 7 dígitos e não tem o traço separador')
    print('Acrescenta-se o 3 e o separador.')
    print("Sem formatação: "+ '3'+telefone[0:3]+telefone[3:])
    print("Com formatação: "+ '3'+telefone[0:3] + '-' +telefone[3:])

elif telefone.isdigit() and tam == 8 and '-' not in telefone and telefone[0] == '3':
    print('Telefone possui 8 dígitos mas está sem o separador.')
    print('Acrescenta-se o separador')
    print("Sem Formatação: "+ telefone[0:4]+telefone[4:])
    print("Com Formatação: "+ telefone[0:4] + '-' + telefone[4:])

elif telefone[0:4].isdigit() and '-' in telefone and telefone[5:].isdigit() and tam == 9 and telefone[0] == '3':
    print(f'O telefone {telefone} está corretamente formatado.')

else:
    print('Telefone Inválido!')