#Modo 1

##maiorNumero = 0
##for i in range(1,6):
##    if i > maiorNumero:
##        maiorNumero = i
##    print(f'{i}')
##print()
##print(f'Maior número lido na sequência: {maiorNumero}')

#Modo 2
maiorNumero = 0
for i in range(1,6):
    num = int(input(f'Digite o {i}º número: '))
    if num > maiorNumero:
        maiorNumero = num
    print(f'{num}')
print()
print(f'Maior número da sequência: {maiorNumero}')

              
