#138 - Número Primo [Modo For]

menor = int(input('Inicial: '))
maior = int(input('Final: '))
if menor >= maior:
    print('O número final não pode ser menor ou igual ao inicial.')
else:
    for num in range(menor, maior+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(f'{num} é primo!')

