#135 - O Escolhido

N = int(input())
maiorNota = 0.0
alMaior = 0

for k in range(N):
    Mat, Nota = input().split()
    if float(Nota) > maiorNota:
        maiorNota = float(Nota)
        alMaior = int(Mat)
if maiorNota >= 8.0:
    print(alMaior)
else:
    print('Minimum note not reached')



