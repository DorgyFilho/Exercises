#155 - Guilherme e Suas Pipas

def Pipa(num):
    Calculo = ((num - 3)*num)/2
    Resultado = int(Calculo)
    return Resultado

def Main():
    num = int(input())
    print(Pipa(num))

Main()