#076 - Sequências Crescentes

while True:
    num = int(input(''))
    if num == 0:
        break
    res = ''
    for i in range(1, num+1):
        res += str(i) + ' '
    print(res[:-1])


