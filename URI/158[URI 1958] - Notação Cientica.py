#158 - Notação Científica

def notacao(num):
    return '%+.4E' %num

num = float(input())
print(notacao(num))