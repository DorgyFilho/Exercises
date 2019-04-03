#018 - Cédulas

valor = int(input())
val = valor
cem = cinq = vin = dez = cin = dois = um = 0

if int(valor/100) >= 1:
    cem = int(valor/100)
    valor -= cem*100

if int(valor/50) >= 1:
    cinq = int(valor/50)
    valor -= cinq*50

if int(valor/20) >= 1:
    vin = int(valor/20)
    valor -= vin*20

if int(valor/10) >= 1:
    dez = int(valor/10)
    valor -= dez*10

if int(valor/5) >= 1:
    cin = int(valor/5)
    valor -= cin*5

if int(valor/2) >= 1:
    dois = int(valor/2)
    valor -= dois*2

if int(valor/1) >= 1:
    um = int(valor/1)
    valor -= um*1

print('%d' %val)
print('%d nota(s) de R$ 100,00' %cem)
print('%d nota(s) de R$ 50,00' %cinq)
print('%d nota(s) de R$ 20,00' %vin)
print('%d nota(s) de R$ 10,00' %dez)
print('%d nota(s) de R$ 5,00' %cin)
print('%d nota(s) de R$ 2,00' %dois)
print('%d nota(s) de R$ 1,00' %um)

