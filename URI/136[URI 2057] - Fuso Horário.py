#136 - Fuso Horário

S, T, F = map(int, input().split())

if S == 0:
    S += 24

H = S + T + F

if H == 24:
    H = 0
    print(H)

elif H > 24:
    H -= 24
    print(H)

else:
    print(H)