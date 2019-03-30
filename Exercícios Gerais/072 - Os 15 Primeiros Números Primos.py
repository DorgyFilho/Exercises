#072 - Os 15 Primeiros Números Primos

menor = int(input('Digite um número: '))
maior = int(input('Digite outro número: '))
count = 0
for num in range(menor, maior+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(f'{num} é primo')
            count += 1
            if count == 15:
                break
