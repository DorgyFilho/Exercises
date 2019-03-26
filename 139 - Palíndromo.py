#139 - Um Número é Palindromo?

num = int(input('Digite o número a ser verificado: '))
num = str(num)
i = 0
f = len(num)-1
while f > i and num[i] == num[f]:
    i += 1
    f -= 1
if num[i] == num[f]:
    print(f'{num} é palíndromo')
else:
    print(f'{num} não é palíndromo')
