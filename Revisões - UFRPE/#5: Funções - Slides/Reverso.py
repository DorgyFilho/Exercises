#004 - Número Reverso

def reverso(num):
    num = str(num)
    rev = ''

    for i in num:
        rev = i + rev
    return rev