#169 - Dígitos

def Digit(b, p):
    total = b**p
    total = str(total)
    QtdDigit = len(total)
    return QtdDigit

def Main():
    Cases = int(input())
    while Cases > 0:
        b, p = map(int, input().split())
        print(Digit(b, p))
        Cases -= 1

Main()

