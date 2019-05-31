#002 - Funcionário

class Func():

    def __init__(self, nome, sal):
        self.nome = nome
        self.sal = sal

    def pegaNome(self):
        return self.nome
    
    def pegaSalario(self):
        return self.pegaSalario
    
    def __repr__(self):
        return ('Nome: %s\nSalário: R$%.2f' %(self.nome, self.sal))
    
