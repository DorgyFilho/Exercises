#005 - MDC Recursivo

def MDC(a,b):
    if b == 0:
        return a
    else:
        resultado = MDC(b, a%b)
    return resultado