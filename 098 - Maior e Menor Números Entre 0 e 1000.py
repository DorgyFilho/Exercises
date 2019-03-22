#098 - Maior e Menor Números Entre 0 e 1000

maior = 0
menor = 9999
somaMaiorMenor = 0
inicio = int(input('Número Inicial: '))
fim = int(input('Número Final: '))
if inicio <= 0 or fim >= 1000:
    print('Inválido')
else:
    for i in range(inicio, fim+1):
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        somaMaiorMenor = maior + menor
            
print(f'Maior: {maior}\nMenor: {menor}\nSoma Entre Maior e Menor: {somaMaiorMenor}')
