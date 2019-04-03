#021 - Notas e Moedas

valor = eval(input(''))
cem = cinq = vin = dez = cin = dois = um = 0
cinqcents = vincents = dezcents = cincents = umcent = 0

valor = float('%.2f' %valor)
if int(valor/100) >= 1:
    cem = int(valor/100)
    valor -= cem*100

valor = float('%.2f' %valor)
if int(valor/50) >= 1:
    cinq = int(valor/50)
    valor -= cinq*50

valor = float('%.2f' %valor)
if int(valor/20) >= 1:
    vin = int(valor/20)
    valor -= vin*20

valor = float('%.2f' %valor)
if int(valor/10) >= 1:
    dez = int(valor/10)
    valor -= dez*10

valor = float('%.2f' %valor)
if int(valor/5) >= 1:
    cin = int(valor/5)
    valor -= cin*5

valor = float('%.2f' %valor)
if int(valor/2) >= 1:
    dois = int(valor/2)
    valor -= dois*2

valor = float('%.2f' %valor)    
if int(valor/1) >= 1:
    um = int(valor/1)
    valor -= um*1

valor = float('%.2f' %valor)
if int(valor/0.50) >= 1:
    cinqcents = int(valor/0.50)
    valor -= cinqcents*0.50

valor = float('%.2f' %valor)
if int(valor/0.25) >= 1:
    vincents = int(valor/0.25)
    valor -= vincents*0.25

valor = float('%.2f' %valor)
if int(valor/0.10) >= 1:
    dezcents = int(valor/0.10)
    valor -= dezcents*0.10

valor = float('%.2f' %valor)
if int(valor/0.05) >= 1:
    cincents = int(valor/0.05)
    valor -= cincents*0.05

valor = float('%.2f' %valor)
if int(valor/0.01) >= 1:
    umcent = int(valor/0.01)
    valor -= umcent*0.01

print('NOTAS:')
print('%d nota(s) de R$ 100.00' %cem)
print('%d nota(s) de R$ 50.00' %cinq)
print('%d nota(s) de R$ 20.00' %vin)
print('%d nota(s) de R$ 10.00' %dez)
print('%d nota(s) de R$ 5.00' %cin)
print('%d nota(s) de R$ 2.00' %dois)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %um)
print('%d moeda(s) de R$ 0.50' %cinqcents)
print('%d moeda(s) de R$ 0.25' %vincents)
print('%d moeda(s) de R$ 0.10' %dezcents)
print('%d moeda(s) de R$ 0.05' %cincents)
print('%d moeda(s) de R$ 0.01' %umcent)