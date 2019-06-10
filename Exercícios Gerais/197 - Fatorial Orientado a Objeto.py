#197 - Fatorial Orientado a Objeto

class Fatorial:

    def __init__(self):
        self.fat = 1

    def calculaFatorial(self, valor):
        numero = valor
        self.num = numero
        while self.num > 0:
            self.fat *= self.num
            self.num -= 1
        return 'O fatorial de %d é %d' %(numero, self.fat)

n = int(input('Número: '))
Result = Fatorial()
print(Result.calculaFatorial(n))
