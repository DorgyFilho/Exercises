#112 - Construindo Casas

while True:
    K = [int(k) for k in input().split()]
    if K[0] == 0:
        break
    a = K[0]*K[1]
    b = 0
    while b*b*K[2]/100 <= a:
        b += 1
    print(b-1)
