#151 - Tuitando

def Tweet(texto):
    if len(texto) <= 140:
        return 'TWEET'
    else:
        return 'MUTE'

def Menu():
    Texto = input()
    print(Tweet(Texto))

Menu()