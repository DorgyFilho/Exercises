#095 - Fibonacci

n = int(input('Digite o número para gerar a sequência: '))
a,b = 0, 1
while b < n:
    print(b, end=' ')
    a, b = b, a+b

