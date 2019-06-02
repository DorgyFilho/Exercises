#016 - RPG de Mesa

class Ficha():

    def __init__(self, player, char):
        self.__Player = player
        self.__Char = char
        self.__ptsAtt = 5
        self.__ptsHab = 10
        self.__Att = {'Físicos':0, 'Mentais':0, 'Sociais':0}
        self.__Hab = {'Liderança':0, 'Tecnologia':0, 'Magia':0, 'Persuasão':0, 'Medicina':0}
    
    def setPlayer(self, jogador):
        self.__Player = jogador

    def getPlayer(self):
        return self.__Player
    
    def setChar(self, personagem):
        self.__Char = personagem

    def getChar(self):
        return self.__Char

    def getAtt(self):
        return self.__Att
    
    def getHab(self):
        return self.__Hab
    
    def getPtsAtt(self):
        return self.__ptsAtt

    def setPtsHab(self, ponto):
        self.__ptsHab = ponto

    def getPtsHab(self):
        return self.__ptsHab
    
    def setAtbEspec(self, att, pts):
        if att in self.__Att:
            self.__Att[att] = pts
    
    def getAtbEspec(self, att):
        if att in self.__Att:
            return self.__Att[att]
    
    def setHabEspec(self, hab, pts):
        if hab in self.__Hab:
            self.__Hab[hab] = pts
    
    def getHabEspec(self, H):
        if H in self.__Hab:
            return self.__Hab[H]
    
    def addHab(self, nova):
        if nova not in self.__Hab:
            self.__Hab[nova] = 0
        else:
            print('Habilidade já consta no sistema.')
    
    def addPtsHab(self, hab):
        if self.getPtsHab() > 0:
            self.setPtsHab(self.getPtsHab()-1)
            pontos = self.getHabEspec(hab)
            self.setHabEspec(hab, self.getHabEspec(hab)+1)

    def imprimirFicha(self):
        print('Nome: %s' %self.getPlayer())
        print('Char: %s' %self.getChar())
        print('Atributos: %s' %self.getAtt())
        print('Habilidades: %s' %self.getHab())

Dorgival = Ficha('Dorgival', 'Mago')
Dorgival.setAtbEspec('Mentais', 10)
Dorgival.addPtsHab('Magia')
print(Dorgival.getAtbEspec('Mentais'))
print(Dorgival.getHab())
print(Dorgival.getAtt())
print(Dorgival.getHabEspec('Magia')+2)
print()
Dorgival.imprimirFicha()
