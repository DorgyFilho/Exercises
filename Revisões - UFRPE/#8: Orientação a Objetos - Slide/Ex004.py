#004 - Aluno

class Aluno():

    def __init__(self, nome, curso, TSD):
        self.nome = nome
        self.curso = curso
        self.TSD = TSD

    def Estudar(self, qtdeHSD):
        self.TSD += qtdeHSD
        return self.TSD
    
    def Dormir(self, qtdeHSono):
        self.TSD -= qtdeHSono
        return self.TSD

# nome = input('Nome: ')
# curso = input('Curso: ')
# TSD = int(input('Tempo Sem Dormir: '))
# print()
# Estudante = Aluno(nome, curso, TSD)
# print('%d Horas' %Estudante.Estudar(12))
# print()
# print('%d Horas' %Estudante.Dormir(5))