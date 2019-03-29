#010 - Eleições Presidenciais.

Dorgival = 0
Himari = 0
Cecilia = 0
Brancos = 0
Nulos = 0
Total = 0

for i in range(1,16):
    voto = int(input('Digite o seu voto - 1.Dorgival, 2.Himari, 3.Cecilia, 4.Brancos: '))
    if voto == 1:
        Dorgival += 1
    elif voto == 2:
        Himari += 1
    elif voto == 3:
        Cecilia += 1
    elif voto == 4:
        Brancos += 1
    else:
        Nulos += 1
    Total += 1

vtDorgival = (Dorgival/Total)*100
vtHimari = (Himari/Total)*100
vtCecilia = (Cecilia/Total)*100
vtBrancos = (Brancos/Total)*100
vtNulos = (Nulos/Total)*100

print()
print(f'Total de votantes: {Total}')
print(f'Dorgival: {Dorgival} ---> {vtDorgival:.2f}%')
print(f'Himari: {Himari} ---> {vtHimari:.2f}%')
print(f'Cecilia: {Cecilia} ---> {vtHimari:.2f}%')
print(f'Brancos: {Brancos} ---> {vtBrancos:.2f}%')
print(f'Nulos: {Nulos} ---> {vtNulos:.2f}%')