#004 - Teste 004

from Ex004 import *

Humano = Pessoa('João', 19, 77, 1.85)
Humano.envelhecer(10)
Humano.emagrecer(10)
Humano.engordar(5)
Humano.crescer(0.05)
print(Humano)