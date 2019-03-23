#118 - Salário Anual

anoAtual = int(input('Ano Atual: '))
salario = 1000
perc = 1.5
novoSalario = salario + (salario*(perc/100))

for i in range(1997, anoAtual+1):
    perc *= 2
    novoSalario = novoSalario + (novoSalario*(perc/100))
    print(f'Ano: {i} ----> R${novoSalario:.2f}')
