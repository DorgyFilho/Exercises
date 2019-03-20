#037 - Salário Mensal - Modo Completo

sBruto = int(input('Salário Bruto: '))
IR = (11/100)*sBruto
INSS = (8/100)*sBruto
Sind = (5/100)*sBruto
sLiq = sBruto - IR - INSS - Sind

horas = 8
salarioDia = sBruto/30
salarioHora = salarioDia/horas
hMensal = horas*30

print(f'Salário Bruto: R${sBruto:.2f} ---> Salário Líquido: R${sLiq:.2f}')
print(f'Horas Mensais: {hMensal}')
print(f'Salário-Dia (Calculado usando o Salário Bruto como referência: R${salarioDia:.2f}')
print(f'Salário-Hora(Salário Bruto como Referência): R${salarioHora:.2f}')
