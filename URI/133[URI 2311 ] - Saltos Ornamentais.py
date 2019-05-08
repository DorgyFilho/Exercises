#133 - Saltos Ornamentais

Players = int(input())

for player in range(Players):
    nome = input()
    gDif = float(input())

    Nota = input().split()
    for k in range(len(Nota)):
        Nota[k] = float(Nota[k])
    Nota.sort()
    maior = max(Nota)
    menor = min(Nota)
    Nota.remove(maior)
    Nota.remove(menor)
    
    soma = sum(Nota)
    somaComPeso = soma*gDif

    print('{} {:.2f}'.format(nome, somaComPeso))
