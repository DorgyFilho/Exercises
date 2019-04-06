#080 - Fatorial Simples

fat = 1
N = int(input(''))
while N > 0:
    fat *= N
    N -= 1
print(fat)