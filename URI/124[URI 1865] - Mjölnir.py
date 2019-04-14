#124 - Mjölnir

T = int(input())

for i in range(T):
    Info = input().split()
    Name = str(Info[0])
    Strength = int(Info[1])
    if Name == 'Thor':
        print('Y')
    else:
        print('N')