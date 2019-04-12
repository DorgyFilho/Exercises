#006 - Eleições OS

OS = ['Win XP', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outros']
Votos = [0]*6
Total = 0
print('1-Win XP, 2-Unix, 3-Linux, 4-Netware, 5-Mac OS, 6-Outro')
print()
voto = ''
while voto != 0:
    voto = int(input('Digite o seu voto: '))
    if not (1 <= voto <= 6):
        print('Candidato Indisponível. Tente Novamente.')
        continue
    if voto == 0:
        break
    Votos[voto-1] += 1
    Total += 1

k = 0
maisVotado = 0
for y in range(len(OS)):
    print(f'{OS[k]} --- {Votos[k]} --- {(Votos[k]/float(Total)*100):.2f}%')
    print()
    if Votos[k] > Votos[maisVotado]:
        maisVotado = k
    k += 1

print(f'Total: {Total}')
print()
print(f'O Sistema Operacional mais votado foi {OS[maisVotado]} com {Votos[maisVotado]} votos, correspondendo a {(Votos[maisVotado]/float(Total)*100):.2f}% dos votos')