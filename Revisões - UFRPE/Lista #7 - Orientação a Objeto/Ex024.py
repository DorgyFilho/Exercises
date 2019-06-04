#024 - Exercício Extra 24: Aluno 2

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
            return 'Equipe Criada!'
        else:
            return 'Equipe não pode ser criada!'

p1 = Aluno('Dorgy', '1234')
p2 = Aluno('Akiza', '5678')
team1 = Equipe('Dragon-Lotus')
team1.addMembro(p1)
team1.addMembro(p2)
Org = Gerenciamento()
print(Org.Criar(team1))
p3 = Aluno('Cecilia', '4321')
p4 = Aluno('Alexis', '9876')
team2 = Equipe('Dragon-Honda')
team2.addMembro(p3)
team2.addMembro(p4)
print(Org.Criar(team2))
team3 = Equipe('Dragon-Lotus')
team3.addMembro(p1)
team3.addMembro(Aluno('Simona', '7878'))
print(Org.Criar(team3)) 
