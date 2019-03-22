#096 - Fibonacci Até o Número 500

a, b = 0, 1

while b < 500:
    print(b, end=' ')
    a, b = b, a+b
