import random 
def crearMatriz(n,matriz = []):#O(n**2)
  for i in range(n): 
    matriz.append([])
    [matriz[i].append(random.randint(1,99)) for j in range(n)]
  return sumaTotal(matriz),Mostrar(matriz)
def Mostrar(matriz):  #O(n)
  [print(x) for x in matriz]
def sumaTotal(lista,suma=0): #O(n) 
  for i in lista: suma+=sum(i)
  return suma
crearMatriz(4)[0]
