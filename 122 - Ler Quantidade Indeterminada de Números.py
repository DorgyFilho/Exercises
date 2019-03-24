entre0e25 = 0
entre26e50 = 0
entre51e75 = 0
entre76e100 = 0

while True:
    num = int(input('Digite um número: '))
    if num <= 0 or num > 100:
        print('Encerrado!')
        break
    else:
        if 0 <= num <= 25:
            entre0e25 += 1
        elif 26 <= num <= 50:
            entre26e50 += 1
        elif 51 <= num <= 75:
            entre51e75 += 1
        else:
            entre76e100 += 1

print(f'[0-25]: {entre0e25}\n[26-50]: {entre26e50}\n[51-75]: {entre51e75}\n[76-100]: {entre76e100}')