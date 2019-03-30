#007 - Recolhimento de CPMF

valorCheque = int(input('Valor de um cheque: '))
taxaCPMF = (0.3/100)
impRecolher = valorCheque*taxaCPMF
print(f'O imposto a recolher é R${impRecolher:.2f}')