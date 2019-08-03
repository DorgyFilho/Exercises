#162 - Raiz Quadrada de 10

N=int(input())
Contador=N
x=(1/6)
y=(1/6)
if N == 0:
   print("%.10f" %(3))
else:
    while Contador >= 2:
        y=(1/(6+y))
        Contador = Contador-1
    print("%.10f" %(3+y))