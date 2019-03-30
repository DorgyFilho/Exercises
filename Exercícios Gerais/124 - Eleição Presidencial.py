#124 - Eleição Presidencial

Dorgival = 0
Himari = 0
Joao = 0
Amanda = 0
Brancos = 0
Nulos = 0
Invalido = 0
votosTotais = 0
votosValidos = 0

aptos = int(input('Digite o número de eleitores aptos a votar: '))

for i in range(1, aptos+1):
    voto = input('Digite seu voto - 1.Dorgival, 2.Himari, 3.Joao, 4.Amanda, 5.Brancos: ')
    if voto == '1':
        Dorgival += 1
    elif voto == '2':
        Himari += 1
    elif voto == '3':
        Joao += 1
    elif voto == '4':
        Amanda += 1
    elif voto == '5':
        Brancos += 1
    else:
        Nulos += 1
    
    votosTotais = Dorgival + Himari + Joao + Amanda + Brancos + Nulos
    vtDorgival = (Dorgival/votosTotais)*100
    vtHimari = (Himari/votosTotais)*100
    vtJoao = (Joao/votosTotais)*100
    vtAmanda = (Amanda/votosTotais)*100
    vtBrancos = (Brancos/votosTotais)*100
    vtNulos = (Nulos/votosTotais)*100

    votosValidos = Dorgival + Himari + Joao + Amanda
    ValDorgival = (Dorgival/votosValidos)*100
    ValHimari = (Himari/votosValidos)*100
    ValJoao = (Joao/votosValidos)*100
    ValAmanda = (Amanda/votosValidos)*100

print()
print('ELEIÇÕES PRESIDENCIAIS - VOTOS TOTAIS')
print('='*80)
print(f'Dorgival: {Dorgival} ---> {vtDorgival:.2f}%')
print(f'Himari: {Himari} ---> {vtHimari:.2f}%')
print(f'Joao: {Joao} ---> {vtJoao:.2f}%')
print(f'Amanda: {Amanda} ---> {vtAmanda:.2f}%')
print(f'Brancos: {Brancos} ---> {vtBrancos:.2f}%')
print(f'Nulos: {Nulos} ---> {vtNulos:.2f}%')

print()

print('ELEIÇÕES PRESIDENCIAIS - VOTOS VÁLIDOS(EXCLUEM-SE BRANCOS E NULOS)')
print()
print(f'Dorgival: {Dorgival} ---> {ValDorgival:.2f}%')
print(f'Himari: {Himari} ---> {ValHimari:.2f}%')
print(f'João: {Joao} ---> {ValJoao:.2f}%')
print(f'Amanda: {Amanda} ---> {ValAmanda:.2f}%')
