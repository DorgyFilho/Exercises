#166 - Aproveite a Oferta

Cases = int(input())
for a in range(Cases):
    N,K = map(int, input().split())
    Div = int(N / K)
    Mod = int(N % K)
    Total = Div + Mod
    print('%d' %Total)
