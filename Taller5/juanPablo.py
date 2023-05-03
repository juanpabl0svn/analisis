def DupAdd(numero):
  suma = 0

  if numero %2 == 0:
    suma+=1
    for i in range(1,numero):
      if suma == numero:
        return i
      suma*=2
  else:
    for i in range(numero):
      if suma == numero:
        return i
      if suma * 2 <= numero:
        suma*=2
      if suma + 1 <= numero:
        suma+=1
  return numero


DupAdd(8)



def difAbs(lista1,lista2):
  dif = 0
  lista1,lista2 = sorted(lista1),sorted(lista2)
  for i in range(len(lista1)):
    val = lista1[i] - lista2[i]
    if val < 0:
      dif+=val*-1
    else:
      dif+=val
  return dif

difAbs([4,1,2],[2,4,1])
