#004 - Aluno

class Aluno():

    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.TSD = 0

    def Estudar(self, H):
        self.TSD += H
    
    def Dormir(self, H):
        self.TSD -= H
    
    def SemDormir(self):
        print('Tempo sem dormir: %d horas' %(self.TSD))


# nome = input('Nome: ')
# curso = input('Curso: ')
# TSD = int(input('Tempo Sem Dormir: '))
# print()
# Estudante = Aluno(nome, curso, TSD)
# print('%d Horas' %Estudante.Estudar(12))
# print()
# print('%d Horas' %Estudante.Dormir(5))