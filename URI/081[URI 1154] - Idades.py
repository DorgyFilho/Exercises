#081 - Idades

lID = []
while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        lID.append(idade)

media = sum(lID)/len(lID)

print('%.2f' %media)