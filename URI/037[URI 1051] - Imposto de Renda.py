#037 - Imposto de Renda

renda = float(input(''))

if 0.00 <= renda <= 2000.00:
    print('Isento')
elif 2000.00 < renda <= 3000.00:
    prov = renda - 2000
    taxa = (8/100)*prov
    print('R$ %.2f' %taxa)
elif 3000.00 < renda <= 4500.00:
    prov = renda - 2000
    prov2 = prov - 1000
    taxa1 = (8/100)*1000
    taxa2 = (18/100)*prov2
    tTotal = taxa1 + taxa2
    print('R$ %.2f' %tTotal)
else:
    prov = renda - 2000
    prov2 = prov - 1000
    taxa1 = (8/100)*1000
    prov3 = prov2 - 1500
    taxa2 = (18/100)*1500
    taxa3 = (28/100)*prov3
    tTotal = taxa1 + taxa2 + taxa3
    print('R$ %.2f' %tTotal)