#049 - Loja das Tintas v2

metros = int(input('Quantidade de metros a ser pintada: '))

lts = (metros/6.0)*1.1 #10% de folga.
lat = int(lts/18.0)
gal = int(lts/3.6)

if lts % 18!= 0:
    lat += 1

if lts % 3.6 != 0:
    gal += 1

mLat = int(lts/18.0)
mGal = int((lts - (mLat*18.0))/3.6)
if ((lts - (mLat*18.0) % 3.6 != 0)):
    mGal += 1

vLata = lat*80
vGal = gal*25
vMLat = mLat*80
vMGal = mGal*25

print(f'Latas: {lat} ---> Valor: R${vLata}')
print(f'Galões: {gal} ---> Valor: R${vGal}')
print(f'Mix de latas e galões, respectivamente, {mLat} e {mGal} ---> Respectivos Valores: {vMLat} e {vMGal}')
