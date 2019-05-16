#005 - Fatorial Recursivo

def fatoRec(num):
    if num == 0 or num == 1:
        return 1
    else:
        fat = num*fatoRec(num-1)
    return fat