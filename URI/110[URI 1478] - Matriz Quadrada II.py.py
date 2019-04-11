while True:
  ent = int(input(''))
  if ent == 0:
    break

  principal = []

  for a in range(1, ent+1):
    aux = []
    k = a
    for b in range(1, ent+1):
      aux.append(abs(k))
      if k == 1:
        k -= 3
      else:
        k -= 1
    principal.append(aux)
  
  for c in range(ent):
    temp = ''
    for d in range(ent):
      temp += ' %3d' %principal[c][d]
    print(temp[1:])
  print()