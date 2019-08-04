# #170 - Umil Bolt

while True:
    try:
        Cases = int(input())
        Fastest = 1000.0
        for i in range(Cases):
            Time = float(input())
            if Time < Fastest:
                Fastest = Time
        print(Fastest)
    except EOFError:
        break






