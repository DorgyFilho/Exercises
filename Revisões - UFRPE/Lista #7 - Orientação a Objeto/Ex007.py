#007 - Jogo da Velha

class JogoDaVelha():
    def __init__(self): #Construir tabuleiro com 9 espaços
        self.espaco = [' ']*9
    
    def Tabuleiro(self): #Mostrar tabuleiro na tela
        print(self.espaco[0] + ' | ' + self.espaco[1] + ' | ' + self.espaco[2])
        print('-'*9)
        print(self.espaco[3] + ' | ' + self.espaco[4] + ' | ' + self.espaco[5])
        print('-'*9)
        print(self.espaco[6] + ' | ' + self.espaco[7] + ' | ' + self.espaco[8])
    
    def Atualizar(self, numEspaco, jogador): #PREENCHER TABULEIRO
        if self.espaco[numEspaco-1] == ' ':
            self.espaco[numEspaco-1] = jogador
    
    def Vencedor(self, jogador):
        #Horizontal
        if (self.espaco[0] == jogador and self.espaco[1] == jogador and self.espaco[2] == jogador):
            return True
        if (self.espaco[3] == jogador and self.espaco[4] == jogador and self.espaco[5] == jogador):
            return True
        if (self.espaco[6] == jogador and self.espaco[7] == jogador and self.espaco[8] == jogador):
            return True
        
        #Vertical
        if (self.espaco[0] == jogador and self.espaco[3] == jogador and self.espaco[6] == jogador):
            return True
        if (self.espaco[1] == jogador and self.espaco[4] == jogador and self.espaco[7] == jogador):
            return True
        if (self.espaco[4] == jogador and self.espaco[5] == jogador and self.espaco[8] == jogador):
            return True

        #Diagonal
        if (self.espaco[0] == jogador and self.espaco[4] == jogador and self.espaco[8] == jogador):
            return True
        if (self.espaco[2] == jogador and self.espaco[4] == jogador and self.espaco[6] == jogador):
            return True

    #Limpar o tabuleiro
    def Reiniciar(self):
        self.espaco = [' ']*9
    
    #Houve Empate?
    def Verificar(self):
        ocupado = 0
        for spc in self.espaco:
            if spc != ' ':
                ocupado += 1
        if ocupado == 9:
            return True
        else:
            return False

#Criar objeto  
Jogo = JogoDaVelha()

def BoasVindas():
    print('Bem-vindo(s) ao Jogo da Velha')
    print()
    Jogo.Tabuleiro()

BoasVindas()

while True:
    #Jogador X
    X = int(input('Digite um número de 1 a 9: '))
    Jogo.Atualizar(X, 'X')
    Jogo.Tabuleiro()

    #X é o vencedor?
    if Jogo.Vencedor('X'):
        print('Jogador X Venceu!')
        R = input('Deseja jogar de novo? S/N: ').upper()
        if R == 'S':
            Jogo.Reiniciar()
        else:
            break
        
    #Empatou?
    if Jogo.Verificar():
        print('O jogo terminou empatado!')
        R = input('Deseja jogar de novo? S/N: ').upper()
        if R == 'S':
            Jogo.Reiniciar()
        else:
            break
        
    #Jogador O
    O = int(input('Escolha um número de 1 a 9: '))
    Jogo.Atualizar(O, 'O')
    Jogo.Tabuleiro()
        
    #O é o vencedor?
    if Jogo.Vencedor('O'):
        print('Jogador O venceu!')
        R = input('Deseja jogar de novo? S/N: ').upper()
        if R == 'S':
            Jogo.Reiniciar()
        else:
            break
        
    #Empatou?
    if Jogo.Verificar():
        print('O jogo terminou empatado!')
        R = input('Deseja jogar de novo? S/N: ').upper()
        if R == 'S':
            Jogo.Reiniciar()
        else:
            break


