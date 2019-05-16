#004 - Reverso de um Número

# MÉTODO 1
# def Reverso(num):
#     num = str(num)
#     numRev = num[::-1]
#     return numRev

# num = int(input('Número: '))
# Final = Reverso(num)
# print(Final)

#Método 2
def Rev(num):
    num = str(num)
    tamNum = len(num) - 1
    numRev = ''

    while tamNum >= 0:
        numRev += num[tamNum]
        tamNum -= 1
    return numRev

num = int(input('Número: '))
Final = Rev(num)
print(Final)