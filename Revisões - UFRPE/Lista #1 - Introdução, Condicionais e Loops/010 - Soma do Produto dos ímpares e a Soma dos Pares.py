#010 - Soma do Produto dos Ímpares e a Soma dos Pares

somaProdImp = 0
somaPares = 0
multiImp = 1
num = ''

while num != 9999:
    num = int(input('Digite um número: '))
    if num == 9999:
        print('Encerrado!')
        break
    else:
        if num % 2 == 0:
            somaPares += num
        else:
            multiImp *= num
            somaProdImp += multiImp

print(f'Soma do Produto dos Ímpares: {somaProdImp} ---> Soma dos Pares: {somaPares}')