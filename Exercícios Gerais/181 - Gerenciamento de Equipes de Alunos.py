#181 - Gerenciamento de Equipes de Alunos

class Aluno:

    def __init__(self, N, D):
        self.nome = N
        self.cpf = D
    
class Equipe:

    def __init__(self, P):
        self.projeto = P
        self.Equipe = []
    
    def addMembro(self, novo):
        self.Equipe.append(novo)

class Gerenciamento:

    def __init__(self):
        self.Time = []

    def Criar(self, team):
        Crie = True
        for novo in self.Time:
            if novo.projeto == team.projeto:
                for m1 in team.Equipe:
                    for m2 in team.Equipe:
                        if m1.cpf == m2.cpf:
                            Crie = False
        
        if Crie:
            self.Time.append(team)
            return 'Equipe criada com sucesso!'
        else:
            return 'Equipe não pode ser criada!'


P1 = Aluno('Dorgival', '1234')
P2 = Aluno('Simona', '7878')
P3 = Aluno('Katherine', '4321')
Team1 = Equipe('Dragon-Lotus')
Team1.addMembro(P1)
Team1.addMembro(P2)
Team1.addMembro(P3)
Org = Gerenciamento()
print(Org.Criar(Team1))
print()
Team2 = Equipe('Dragon-Honda')
P4 = Aluno('Danica', '7765')
P5 = Aluno('Sebastian', '8765')
P6 = Aluno('Daniel', '4567')
Team2.addMembro(P4)
Team2.addMembro(P5)
Team2.addMembro(P6)
print(Org.Criar(Team2))
Team1.addMembro(P1)
print()
print(Org.Criar(Team1))
    
