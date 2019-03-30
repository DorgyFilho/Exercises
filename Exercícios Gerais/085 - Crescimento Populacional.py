#085 - Crescimento Populacional

paisA = 80000
paisB = 200000
taxaA = (3/100)
taxaB = (1.5/100)

anos = 0

while paisA < paisB:
    paisA *= (1+taxaA)
    paisB *= (1+taxaB)
    anos += 1

print(f'Pais A: {paisA:.0f}\nPaís B: {paisB:.0f}\nQuantidade de anos para A passar B: {anos} anos')
