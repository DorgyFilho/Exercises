#163 -  O Enigma de Pronalândia

def Enigma(num):
    value = str(num)
    reversedValue = value[::-1]
    # reversedValue = int(reversedValue)
    return '%s' %reversedValue

num = input().strip()
print(Enigma(num))