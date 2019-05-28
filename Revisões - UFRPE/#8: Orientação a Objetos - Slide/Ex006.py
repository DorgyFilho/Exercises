#006 - Alunos 2

class Aluno():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
class Equipe():

    def __init__(self, projeto):
        self.listaAlunos = []
        self.projeto = projeto

    def addAluno(self, novoAluno):
        self.listaAlunos.append(novoAluno)

class GerenciarEquipes():
    
    def __init__(self):
        self.Equipes = []

    def criarEquipe(self, team):
        Crie = True
        for novo in self.Equipes:
            if novo.projeto == team.projeto:
                for mbm1 in team.listaAlunos:
                    for mbm2 in novo.listaAlunos:
                        if mbm1.cpf == mbm2.cpf:
                            Crie = False
        if Crie:
            self.Equipes.append(team)
            return 'Equipe Criada'
        else:
            return 'Equipe não pode ser criada'

p1 = Aluno('Dorgy', '1234')
p2 = Aluno('Akiza', '5678')
team1 = Equipe('Dragon-Lotus')
team1.addAluno(p1)
team1.addAluno(p2)
Org = GerenciarEquipes()
print(Org.criarEquipe(team1))
p3 = Aluno('Cecilia', '4321')
p4 = Aluno('Alexis', '9876')
team2 = Equipe('Dragon-Lotus')
team2.addAluno(p3)
team2.addAluno(p4)
print(Org.criarEquipe(team2))
team3 = Equipe('Dragon-Lotus')
team3.addAluno(p1)
team3.addAluno(Aluno('Simona', '7878'))
print(Org.criarEquipe(team3)) 

    
