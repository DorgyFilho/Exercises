#122 - A Resposta de Theon

T = int(input())

K = [int(k) for k in input().split()]

A, B = K[0], 0

for m in range(T):
    if K[m] < A:
        A, B = K[m], m
print(B+1)