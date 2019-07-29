#154 - Corvo Contador


def piscou(pisque):
    pisque = pisque.replace('-','0') #Se for olho fechado, é 0
    pisque = pisque.replace('*','1') #Se for olho aberto, é 1
    return pisque #Retorne o resultado

def intPiscou(pisque):
    pisque = int(pisque, 2)
    return pisque

def total(pisque,total):
    total += pisque
    return total

def Main():
    for i in range(3):
        Total = 0
        while True:
            pisque = input().lower()
            if pisque == 'caw caw':
                print(Total)
                break
            else:
                pisque = piscou(pisque)
                pisque = intPiscou(pisque)
                Total = total(pisque, Total)

Main()


