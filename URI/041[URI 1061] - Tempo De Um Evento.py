#041 - Tempo De Um Evento

info = input().split()
dia = int(info[1])

hor1 = input().split(':')
h1, m1, s1 = list(map(int, hor1))

info2 = input().split()
dia2 = int(info2[1])

hor2 = input().split(':')
h2, m2, s2 = list(map(int, hor2))

d = dia2 - dia
h = h2 - h1
m = m2 - m1
s = s2 - s1

if h < 0:
    h += 24
    d -= 1

if m < 0:
    m += 60
    h -= 1

if s < 0:
    s += 60
    m -= 1

if d <= 0:
    d = 0

print('%d dia(s)' %d)
print('%d hora(s)' %h)
print('%d minuto(s)' %m)
print('%d segundo(s)' %s)



