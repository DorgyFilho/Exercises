from Tempo import conv

num = int(input('Digite um número: '))
normal = 0
if num == 0000:
    normal = '12:00 A.M'
    print(normal)
elif num > 1200:
    normal = conv(num-1200)
    print(normal[0:2] + ':' + normal[2:] + ' P.M')
else:
    normal = conv(num+1200-1200)
    print(normal[0:2] + ':' + normal[2:] + ' A.M')
    