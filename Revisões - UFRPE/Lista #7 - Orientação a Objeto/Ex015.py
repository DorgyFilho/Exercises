#015 - Calendário

class Evento:

    def __init__(self, nome, data, inicio, fim):
        self.__nome = nome
        self.__data = data
        self.__inicio = inicio
        self.__fim = fim
    
    def getData(self):
        return self.__data

    def getInicio(self):
        return self.__inicio
    
    def getFim(self):
        return self.__fim
    
    def getNome(self):
        return self.__nome
    
class Calendario:

    def __init__(self):
        self.__calendario = {}

    def addEvento(self, evento):
        Data = evento.getData()

        if Data not in self.__calendario:
            self.__calendario[Data] = [evento]
            return 'Evento Adicionado!'
        else:
            adicionar = True
            e_inicio = int(evento.getInicio()[0:2])*60+int(evento.getInicio()[3:])
            e_fim = int(evento.getFim()[0:2])*60+int(evento.getFim()[3:])

            for item in self.__calendario[Data]:
                Start = int(item.getInicio()[0:2])*60+int(item.getInicio()[3:])
                End = int(item.getFim()[0:2])*60+int(item.getFim()[3:])

                if e_fim >= End and e_inicio >= End:
                    continue

                elif e_fim <= Start and e_inicio <= Start:
                    continue 
                
                elif e_inicio <= Start and e_fim >= End:
                    adicionar = False
                    break

                elif e_inicio <= Start and (e_fim >= Start and e_fim <= End):
                    adicionar = False
                    break
                
                elif e_fim >= End and (e_inicio >= Start and e_inicio <= End):
                    adicionar = False
                    break
                
                elif (e_inicio >= Start and e_inicio <= End) and (e_fim >= Start and e_fim <= End):
                    adicionar = False
                    break
            
            if adicionar == True:
                self.__calendario[Data].append(evento)
                return 'Evento adicionado!'
            else:
                return 'Evento não pode ser adicionado.'
    
    def removerEvento(self, nome, data):
        if data in self.__calendario:
            for k in self.__calendario[data]:
                if k.getNome() == nome:
                    self.__calendario[data].remove(k)
                    return 'Evento Removido!'
        else:
            return 'Evento não encontrado!'
    
    def Listar(self):
        for elem in self.__calendario:
            print(elem)
            for item in self.__calendario[elem]:
                return('Evento: %s [%s - %s]' %(item.getNome(), item.getInicio(), item.getFim()))
            return ''

e1 = Evento('X', '01/06/2019', '18:00', '23:00')
e2 = Evento('Y', '01/06/2019', '13:00', '17:30')
e3 = Evento('Z', '01/06/2019', '16:00', '17:20')
K = Calendario()
print(K.addEvento(e1))
print(K.addEvento(e2))
print(K.addEvento(e3))                
print(K.removerEvento('Y', '01/06/2019'))
print()
print(K.Listar())