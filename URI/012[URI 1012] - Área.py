#012 - Área

valor = input().split(' ')
a, b, c = valor
pi = 3.14159

tri = (float(a)*float(c))/2
cir = pi*(float(c)*float(c))
trap = float(c)*(float(a)+float(b))/2
qua = float(b)*float(b)
ret = float(a)*float(b)

print('TRIANGULO: %.3f' %tri)
print('CIRCULO: %.3f' %cir)
print('TRAPEZIO: %.3f' %trap)
print('QUADRADO: %.3f' %qua)
print('RETANGULO: %.3f' %ret)