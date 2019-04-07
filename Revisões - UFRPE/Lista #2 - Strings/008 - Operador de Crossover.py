#008 - Operador de Crossover

from random import randint

S1 = 'ATCGCGTA'
S2 = 'TAGAAGAT'

p = randint(0, len(S1))

newS1 = S1[:p] + S2[p:]
newS2 = S2[:p] + S1[p:]

print(f'{newS1}\n{newS2}')