#177 - Pepe, Já Tirei a Vela

Cases = int(input())
while Cases > 0:
    H, M, O = map(int, input().split())
    if O == 1:
        Result = '%02d:%02d' %(H,M)
        print(Result + ' - A porta abriu!')
    elif O == 0:
        Result = '%02d:%02d' %(H,M)
        print(Result + ' - A porta fechou!')
    Cases -= 1
