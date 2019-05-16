#008 - MDC Recursivo

def MDC(a,b):
    if a%b == 0:
        return b
    else:
        resultado = MDC(b, a%b)
    return resultado

a = int(input('Número a: '))
b = int(input('Número b: '))
Final = MDC(a,b)
print(Final)