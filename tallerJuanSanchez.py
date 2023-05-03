def DupAdd(numero):
  suma = 0
  for i in range(0,numero):
    if suma == numero:
      return i+1
    if suma * 2 <= numero:
      suma*=2
    if suma + 1 <= numero:
      suma+=1
  return numero

dupAdd(8)

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
