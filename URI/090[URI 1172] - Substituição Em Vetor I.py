#090 - Substituição Em Vetor I

K = []
for i in range(10):
    num = int(input())
    if num <= 0:
        num = 1
        K.append(num)
    else:
        K.append(num)

    print('X[%d] = %d' %(i, num))