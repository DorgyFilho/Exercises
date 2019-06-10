#198 - Fibonacci Orientado a Objeto

class Fibonacci:

    def __init__(self):
        self.a = 0
        self.b = 1
    
    def calculaFibo(self, num):
        while self.b < num:
            print(self.b, end=' ')
            self.a, self.b = self.b, self.a + self.b

num = int(input('Digite um número: '))
Fib = Fibonacci()
Fib.calculaFibo(num)
