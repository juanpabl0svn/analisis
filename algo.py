import random 
def crearMatriz(n,matriz = []):   #n**2
  for i in range(n): 
    matriz.append([]) 
    for j in range(n): 
      matriz[i].append(random.randint(1,99))
  return Mostrar(matriz)
def Mostrar(matriz):  #n
  [print(x) for x in matriz]
  return sumaTotal(matriz)
def sumaTotal(lista,suma=0): #n  + n
  for i in lista: suma=suma+sum(i)
  return suma
crearMatriz(4)