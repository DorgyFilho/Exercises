#115 - Bob Conduite

T = int(input())

for i in range(T):
    K = input()

    R1, R2 = map(int, K.split())

    print(R1+R2)