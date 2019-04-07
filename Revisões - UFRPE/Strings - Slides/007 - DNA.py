#007 - DNA

DNA = 'AGCT'
RNA = ''

for let in DNA:
    if 'A' in let:
        RNA += 'U'
    if 'G' in let:
        RNA += 'C'
    if 'C' in let:
        RNA += 'G'
    if 'T' in let:
        RNA += 'A'

print(f'{DNA} --> {RNA}')