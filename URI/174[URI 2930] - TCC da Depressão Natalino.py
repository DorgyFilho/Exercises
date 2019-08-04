#174 - TCC da Depressão Natalino

D,F = input().split()
D = int(D)
F = int(F)

if F - D < 0:
    print("Eu odeio a professora!")
elif (F - D) >= 3:
    print("Muito bem! Apresenta antes do Natal!")
elif (F - D) < 3:
    print("Parece o trabalho do meu filho!")
    F += 2
    if F <= 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")

