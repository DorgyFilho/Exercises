#078 - Eleições

a = 0
b = 0
c = 0
nulo = 0
branco = 0
total = 0
for i in range(1,16):
    voto = int(input('Digite o seu voto 1-a, 2-b, 3-c, 4-nulo, 5-branco: '))
    if voto == 1:
        a += 1
    elif voto == 2:
        b += 1
    elif voto == 3:
        c += 1
    elif voto == 4:
        nulo += 1
    elif voto == 5:
        branco += 1
    else:
        print('Opção inválida.')
        continue
    total += 1

percNulo = (nulo/total)*100
percBranco = (branco/total)*100

print(f'Votos para o candidato a: {a}')
print(f'Votos para o candidato b: {b}')
print(f'Votos para o candidato c: {c}')
print(f'Votos Brancos: {branco}')
print(f'Votos Nulos: {nulo}')
print(f'Percentual de votos brancos sobre os votos totais: {percBranco:.2f}%')
print(f'Percentual de votos nulos sobre os votos totais: {percNulo:.2f}%')
