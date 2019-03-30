#141 - FizzBuzz

n = 50
for i in range(n):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
        continue
    elif i % 3 == 0:
        print('fizz')
        continue
    elif i % 5 == 0:
        print('buzz')
        continue
    print(i)
