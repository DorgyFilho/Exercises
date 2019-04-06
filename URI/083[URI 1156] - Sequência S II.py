#083 - Sequência S II

K = 1
W = [x for x in range(2,101) if x % 2 != 0]

for p, e in enumerate(W):
    K += e/(2**(p+1))
print('%.2f' %K)