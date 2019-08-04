#167 - Fibonot

def Fibonot(num):
    a = 1
    b = 2
    c = 3
    while num > 0:
        a = b
        b = c
        c = a + b
        num -= (c - b - 1)
    num += (c - b - 1)
    return b + num

num = int(input())
print(Fibonot(num))
