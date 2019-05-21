#005 - Ranking de Palavras

def Rank():
    ranking = {}
    arq = open(input('Arquivo: '))
    Info = arq.read()
    Info = Info.replace('  ','')
    Palavras = Info.split('\n')
    arq.close()

    for nome in Palavras:
        if nome in ranking:
            qtde = ranking[nome]
            qtde += 1
            ranking[nome] = qtde
        else:
            ranking[nome] = 1

    primeiroLugar = max(ranking.values())
    Info = []
    while primeiroLugar > 0:
        for k, v in ranking.items():
            if v == primeiroLugar:
                Info.append(f'{k} - {v}')
            if len(Info) == 5:
                break
        primeiroLugar -= 1
        if len(Info) == 5:
            break
    print(Info)

Rank()