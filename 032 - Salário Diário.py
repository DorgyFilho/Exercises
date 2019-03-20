#032 - Salário Mensal
#Considerarei o mês contábil, composto por 30 dias.
#Carga horária de trabalho: 8 horas por dia.
horas = 8
salario = int(input('Salário: '))
salarioDia = salario/30
salarioHora = salarioDia/horas
horasMensais = 30*horas

print(f'Número de horas trabalhadas no mês: {horasMensais}\nSalário Por Hora: {salarioHora:.2f}')


