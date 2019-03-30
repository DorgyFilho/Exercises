#074 - Valores Positivos

count = 5
num = ''
result = ''
while count > 0:
    num = int(input('Digite o número: '))
    if num < 0:
        print('Programa Encerrado!')
        break
    else:
        num = str(num) + ' '
        result += num
        print(result)
    count -= 1