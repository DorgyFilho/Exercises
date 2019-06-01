#008 - Funcionário

class Func():

    def __init__(self, nome, salario, ndpto, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__ndpto = ndpto
        self.__cargo = cargo
    
    def getNome(self):
        return self.__nome

    def getSalario(self):
        return self.__salario
    
    def getDpto(self):
        return self.__ndpto
    
    def getCargo(self):
        return self.__cargo
    
    def setNome(self, N):
        self.__nome = N
    
    def setSalario(self, S):
        self.__salario = S

    def setNDpto(self, D):
        self.__ndpto = D
    
    def setCargo(self, C):
        self.__cargo = C

    def apagaNome(self):
        del self.__nome  

class setorPessoal():

    def __init__(self):
        self.__plantel = []
    
    def addFunc(self, novo):
        self.__plantel.append(novo)
    
    def mostrarFolha(self):
        for pessoa in self.__plantel:
            print('Nome: %s ---> Salário: R$%.2f' %(pessoa.getNome(), pessoa.getSalario()))

    def totalFolhaPgto(self):
        total = 0
        for pessoa in self.__plantel:
            total += pessoa.getSalario()
        return total
    
    def MaiorSalario(self):
        nome = ''
        salario = 0
        for pessoa in self.__plantel:
            if pessoa.getSalario() > salario:
                salario = pessoa.getSalario()
                nome = pessoa.getNome()
        return nome


Pessoa = Func('Dorgival', 12100, 'Administrativo', 'Presidente')
Pessoa2 = Func('Cecilia', 12000, 'Administrativo', 'Vice-Presidente')
Pessoal = setorPessoal()
Pessoal.addFunc(Pessoa)
Pessoal.addFunc(Pessoa2)
print()
Pessoal.mostrarFolha()
print()
print(Pessoal.totalFolhaPgto())
print()
print(Pessoal.MaiorSalario())
   
        

