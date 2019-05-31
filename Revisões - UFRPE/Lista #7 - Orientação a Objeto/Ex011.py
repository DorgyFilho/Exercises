#011 - Casas Inteligentes

class Casa():

    def __init__(self, porta, janela, acender, apagar):
        self.porta = porta
        self.janela = janela
        self.acender = acender
        self.apagar = apagar
    
    def abrirPorta(self, abrir):
        self.porta = abrir
        return self.porta
    
    def fecharPorta(self, fechar):
        self.porta = fechar
        return self.porta
    
    def abrirJanela(self, A):
        self.janela = A
        return self.janela
    
    def fecharJanela(self, F):
        self.janela = F
        return self.janela
    
    def acenderLuzExt(self, Hora, On):
        if 18 <= Hora <= (27-24):
            self.acender = On
        return self.acender
    
    def apagarLuzExt(self, Hora, Off):
        if 3 <= Hora < 18:
            self.apagar = Off
        return self.apagar
    
    def acenderLuzInt(self, Hora, On):
        if Hora < 3 and Hora >= 18:
            self.acender = On
        return self.acender
    
    def apagarLuzInt(self, Hora, Off):
        if Hora >= 3 and Hora < 18:
            self.apagar = Off
        return self.apagar

Resultado = Casa('Sim', 'Sim', 'Sim', 'Não')
print(Resultado.acenderLuzExt(19, 'Sim'))
print(Resultado.apagarLuzExt(8, 'Sim'))
print(Resultado.abrirJanela('Sim'))
print(Resultado.fecharJanela('Não'))
print(Resultado.abrirPorta('Sim'))
print(Resultado.fecharPorta('Sim'))
print(Resultado.acenderLuzInt(19, 'Sim'))
print(Resultado.apagarLuzInt(10, 'Sim'))


    
