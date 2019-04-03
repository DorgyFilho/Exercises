#019 - Conversão de Tempo

seg = int(input(''))

min = int(seg/60)
seg -= min*60
hora = int(min/60)
min -= hora*60

print(repr(hora) + ':' + repr(min) + ':' + repr(seg))
