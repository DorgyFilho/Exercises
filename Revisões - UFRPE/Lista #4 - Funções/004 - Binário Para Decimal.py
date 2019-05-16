#004 - Binário Para Decimal
# Método 1

# def bin2dec(num):
#     Result = 0
#     for bit in num:
#         Result *= 2
#         if bit == '1':
#             Result += 1
#     return Result

#Método 2

def bin2dec(num):
    return sum([int(num[-k])*2**(k-1) for k in range(1, len(num)+1)])

num = input('Número Binário: ')
Final = bin2dec(num)
print(Final)