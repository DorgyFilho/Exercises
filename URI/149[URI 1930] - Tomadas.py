#149 - Tomadas

def Tomadas():
    a,b,c,d = map(int, input().split())
    return a,b,c,d

def calculo(a,b,c,d):
    return a + b + c + d - 3

def main():
    a,b,c,d = Tomadas()
    print(calculo(a,b,c,d))

main()

