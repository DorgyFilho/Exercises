#003 - Positivo ou Negativo

def PouN(num):
    return 'P' if num > 0 else 'N'

num = int(input('Número: '))
Result = PouN(num)
print(Result)