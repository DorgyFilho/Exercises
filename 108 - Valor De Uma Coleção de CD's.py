#108 - Valor De Uma Coleção de CD's

qtdCDs = int(input("Quantidade de CD's adquirida: "))
vMedio = 0
soma = 0

for i in range(1, qtdCDs+1):
    preco = float(input(f'Informe o preço do {i}° CD: '))
    soma += preco
    vMedio = soma/i
    print(f"{i}, '--->', {preco:.2f}")
    print()
print(f"Quantidade de CD's: {qtdCDs}\nTotal Investido: R${soma:.2f}\nPreço Médio da Coleção: R${vMedio:.2f}")
