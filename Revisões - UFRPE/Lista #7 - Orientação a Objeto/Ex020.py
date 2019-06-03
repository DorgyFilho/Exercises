#020 - Questão Extra 3: Bichinho Virtual

from random import randrange

class Pet:

    LvInicialFome = 10
    LvInicialTedio = 5
    DecrescFome = 4
    DecrescTedio = 6
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
            return 'feliz'
        elif self.fome > self.LvInicialFome:
            return 'com fome'
        else:
            return 'entediado'
    
    def __str__(self):
        status = 'Meu nome é %s.' %self.nome
        status += ' Eu estou ' + self.Humor() + '.'
        return status   
    
    def reduzTedio(self):
        self.tedio = max(0, self.tedio - self.LvInicialTedio)
    
    def reduzFome(self):
        self.fome = max(0, self.fome - self.LvInicialFome)
    
    def Saudacao(self):
        print(self.Som[randrange(len(self.Som))])
        self.reduzTedio()

    def Ensinar(self, novoCmd):
        self.Som.append(novoCmd)
        self.reduzTedio()

    def Alimentar(self):
        self.reduzFome()

Filho = Pet('Black Rose Dragon')
print(Filho)
print()
for k in range(15):
    Filho.Relogio()
    print(Filho)
print()
Filho.Alimentar()
Filho.Saudacao()
Filho.Ensinar('Boo!')
Filho.Ensinar('Bom dia!')
Filho.Ensinar('Boa tarde!')
Filho.Ensinar('Boa noite!')
Filho.Ensinar('Meu amor!')
print(Filho.Humor())
print()
for i in range(10):
    Filho.Saudacao()
print(Filho)
