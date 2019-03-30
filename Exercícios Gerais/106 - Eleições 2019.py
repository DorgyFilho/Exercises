#106 - Eleições 2019

totEleitores = int(input('Total de aptos a votar: '))
Joao = 0
Maria = 0
Dorgival = 0
Brancos = 0
Nulos = 0

for i in range(1, totEleitores+1):
    voto = input('Em quem você vota? 1-João, 2-Maria, 3-Dorgival, 4-Brancos: ')
    if voto == '1':
        Joao += 1
    elif voto == '2':
        Maria += 1
    elif voto == '3':
        Dorgival += 1
    elif voto == '4':
        Brancos += 1
    else:
        Nulos += 1

votosValidos = Joao + Maria + Dorgival
validosJoao = Joao/votosValidos
validosMaria = Maria/votosValidos
validosDorgival = Dorgival/votosValidos

print('Contagem dos Votos - Votos Totais')
print()
print(f'Joao: {Joao} votos ----> {(Joao/totEleitores)*100:.2f}%')
print()
print(f'Maria: {Maria} votos ----> {(Maria/totEleitores)*100:.2f}%')
print()
print(f'Dorgival: {Dorgival} votos ----> {(Dorgival/totEleitores)*100:.2f}%')
print()
print(f'Brancos: {Brancos} votos ----> {(Brancos/totEleitores)*100:.2f}%')
print()
print(f'Nulos: {Nulos} votos ----> {(Nulos/totEleitores)*100:.2f}%')
print()

print('ELEIÇÕES 2019 --- VOTOS VÁLIDOS')
print()
print(f'João: {Joao} votos ----> {validosJoao*100:.2f}%')
print()
print(f'Maria: {Maria} votos ----> {validosMaria*100:.2f}%')
print()
print(f'Dorgival: {Dorgival} votos ----> {validosDorgival*100:.2f}%')
    

