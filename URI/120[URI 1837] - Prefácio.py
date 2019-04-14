# #118 - Prefácio

n, d = map(int, input().split())

div = divmod(n, abs(d))

if d < 0:
    print(-div[0], div[1])
else:
    print(div[0], div[1])
