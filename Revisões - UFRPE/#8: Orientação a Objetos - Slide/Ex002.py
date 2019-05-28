#002 - Funcionário

class Funcionario():

    def __init__(self, nome, sal, taxaInc):
        self.func = nome
        self.salario = sal
        self.taxaInc = taxaInc
    
    def NomeFunc(self):
        return self.func
    
    def atualSalario(self):
        return self.salario
    
    def aumento(self):
        incremento = (self.taxaInc/100)*self.salario
        novoSalario = self.salario + incremento
        return novoSalario
    
# nome = input('Seu Nome: ')
# sal = float(input('Salário: '))
# taxa = float(input('Taxa de aumento: '))
# Novo = Funcionario(nome, sal)
# print('Nome: %s\nSalário Atual: R$%.2f\nNovo Salário: R$%.2f' %(Novo.NomeFunc(), Novo.atualSalario(), Novo.aumento()))