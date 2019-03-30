#044 - Diária de um carro

kmPercorridos = int(input('Kms Percorridos: '))
diasAlugados = int(input('Dias alugados: '))

diaria = 60
taxaGasKm = 0.15

precoDia = diaria*diasAlugados
gasRodado= taxaGasKm*kmPercorridos

total = precoDia + gasRodado

print(f'Km Percorridos: {kmPercorridos}\nDias Alugados: {diasAlugados}\nTotal Da Diária: R${precoDia:.2f}\nTotal do Valor da Gasolina Usada no Período: R${gasRodado:.2f}\nTotal a Pagar: R${total:.2f}')
      
