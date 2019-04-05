#048 - Intervalo 2

N = int(input(''))
dentro = 0
fora = 0

for i in range(N):
    X = int(input(''))
    if 10 <= X <= 20:
        dentro +=1
    else:
        fora += 1

print('%d in' %dentro)
print('%d out' %fora)