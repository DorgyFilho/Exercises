#191 - Notas de Aluno

class Aluno:

    def __init__(self, nome, semestre):
        self.nome = nome
        self.sem = semestre
        self.nota = [0]*4
    
    def NomeAluno(self, aluno):
        self.nome = aluno
    
    def pegaAluno(self):
        return self.nome
    
    def obterNota(self, sem, nota):
        self.nota[sem] = nota
    
    def pegaNota(self):
        return self.nota
    
    def definirMedia(self):
        i = 0
        soma = 0
        while i < len(self.nota):
            soma += self.nota[i]
            i += 1
        Media = soma/len(self.nota)
        return Media

nome = input('Nome: ')
serie = int(input('Série: '))
Estudante = Aluno(nome, serie)
i = 0
while i < 4:
    nota = float(input('Nota: '))
    Estudante.obterNota(i, nota)
    i += 1
print('O(a) aluno(a) %s fechou o semestre com média %.2f' %(Estudante.pegaAluno(), Estudante.definirMedia()))

