#184 - Bichinho Virtual

from random import randrange

class Pet:
    
    LvInicialFome = 10
    LvInicialTedio = 5
    DecrescTedio = 6    
    DecrescFome = 4
    Som = ['Aah!']

    def __init__(self, nome):
        self.nome = nome
        self.fome = randrange(self.LvInicialFome)
        self.tedio = randrange(self.LvInicialTedio)
        self.Som = self.Som[:]
    
    def Relogio(self):
        self.tedio += 1
        self.fome += 1

    def Humor(self):
        if self.fome <= self.LvInicialFome and self.tedio <= self.LvInicialTedio:
            return 'feliz!'
        elif self.fome > self.LvInicialFome:
            return 'com fome!'
        else:
            return 'entediado!'
    
    def __str__(self):
        status = 'Meu nome é %s.' %self.nome
        status += ' Eu estou ' + self.Humor() + '.'
        return status
    
    def reduzFome(self):
        self.fome = max(0, self.fome - self.LvInicialFome)
    
    def reduzTedio(self):
        self.tedio = max(0, self.tedio - self.LvInicialTedio)
    
    def Ensinar(self, novo):
        self.Som.append(novo)
        self.reduzTedio()
    
    def Alimentar(self):
        self.reduzFome()
    
    def Saudacao(self):
        print(self.Som[randrange(len(self.Som))])
        self.reduzTedio()

Filho = Pet('Black Rose Dragon')
print(Filho)
print()
for i in range(10):
    Filho.Relogio()
    print(Filho)

for k in range(5):
    Filho.Ensinar(input('Ensine uma saudação: '))

Filho.Saudacao()
Filho.Alimentar()


