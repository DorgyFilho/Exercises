#168 - Festa no Polo Norte

def MDC(Cases):
    Elves = input().split()
    for k in range(Cases):
        Elves[k] = int(Elves[k])
    Elves.sort()
    Maior = int(Elves[Cases-1]) + 1
    while True:
        for b in range(Cases):
            if (Maior % Elves[b]) == 0 and Elves[b] != 1:
                Maior += 1
                break
        Aux = Cases - 1
        if Cases == Aux:
            break
        return Maior

Cases = int(input())
print(MDC(Cases))


