#174 - Número Por Extenso

dezena = 'Zero Dez Vinte Trinta Quarenta Cinqüenta Sessenta Setenta Oitenta Noventa'
unidade = 'um dois três quatro cinco seis sete oito nove'

d = dezena.split()
u = unidade.split()
nd = int(input('Dezena: '))
nu = int(input('Unidade: '))
Nu = nu - 1

if nd == 0 and (0 < Nu <= 9):
    print(f'{u[Nu]}')
if (0 < nd <= 9) and nu == 0:
    print(f'{d[nd]}')
if nd == 1:
    if nu == 1:
        print('Onze')
    elif nu == 2:
        print('Doze')
    elif nu == 3:
        print('Treze')
    elif nu == 4:
        print('Quatorze')
    elif nu == 5:
        print('Quinze')
    elif nu == 6:
        print('Dezesseis')
    elif nu == 7:
        print('Dezessete')
    elif nu == 8:
        print('Dezoito')
    elif nu == 9:
        print('Dezenove')
if (2 <= nd <= 9) and (1 <= nu <= 9):
    print(f'{d[nd]} e {u[Nu]}')