#011 - Eleições OS

votos = [0]*6
OS = ['Win XP', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
voto = ''
total = 0
print('1-Win XP, 2-Unix, 3-Linux, 4-Netware, 5-Mac OS, 6-Outro')

while voto != 0:
    voto = int(input('Digite o seu voto: '))
    if not (1 <= voto <= 6):
        print('Inválido!')
        continue
    if voto == 0:
        print('Eleição Encerrada!')
    votos[voto-1] += 1
    total += 1

k = 0
maisVotado = 0
for y in range(len(OS)):
    print(f'{OS[k]} ---> {votos[k]} ---> {(votos[k]/float(total)*100):.2f}%')
    print()
    if votos[k] > votos[maisVotado]:
        maisVotado = k
    k += 1

print(f'Total de Votos: {total}')
print(f'Vencedor: {OS[maisVotado]}')

