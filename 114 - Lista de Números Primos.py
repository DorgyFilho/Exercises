#114 - Lista de Números Primos

num = int(input('Digite a quantidade de números a ser analisada: '))

for i in range(2, num+1):
    if (i%2 != 0 or i == 2) and (i%3 != 0 or i == 3) and (i%5 != 0 or i == 5) and (i%7 != 0 or i == 7):
        print(i, end=' ')