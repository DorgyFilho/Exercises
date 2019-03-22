#072 - Os 15 Primeiros Números Primos

count = 0
for i in range(2,100):
    if i % 2 == 1:
        count += 1
        if count == 16:
            break
        print(i, end=' ')