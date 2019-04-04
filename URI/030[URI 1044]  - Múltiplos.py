#030 - Múltiplos

linha = input().split(' ')
x = int(linha[0])
y = int(linha[1])

if x%y == 0 or y%x == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')