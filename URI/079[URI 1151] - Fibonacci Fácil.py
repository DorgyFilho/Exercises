#079 - Fibonacci Fácil

a = 0
b = 1
w = int(input())
res = [a, b]

for i in range(2, w):
    k = b + a
    a = b
    b = k
    res.append(k)
print(' '.join(map(str, res)))

