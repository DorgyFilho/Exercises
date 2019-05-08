#134 - Carrega Ou Não Carrega

while True:
    try:
        c = input().split()
        a, b = c
        resultado = int(a)^int(b)
        print(resultado)
    except EOFError:
        break