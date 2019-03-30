#149 - Números Divisíveis Por 5 e 7

for i in range(1500, 2701):
    if i%5 == 0 and i%7 == 0:
        print(str(i))