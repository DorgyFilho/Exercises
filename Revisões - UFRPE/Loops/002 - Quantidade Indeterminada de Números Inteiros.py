#002 - Quantidade Indeterminada de Números Inteiros

num = ''
strNum = ''
while num != 99:
    num = int(input('Digite um número: '))
    if num == 99 or num < 0:
        print('Programa Encerrado!')
        break
    else:
        if num % 2 != 0:
            strNum += str(num) + ' '
            print(strNum)
        else:
            print(strNum)