# def numero(a,b,c):
#     prod = a*b*c
#     return prod

# a = int(input())
# b = int(input())
# c = int(input())

# print(numero(a,b,c))

def fatorial(num):
    fat = 1
    while num > 0:
        fat *= num
        num -= 1
    return fat

num = int(input('Número: '))
result = fatorial(num)
print(result)