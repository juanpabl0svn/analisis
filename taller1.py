import random 
def crearMatriz(fila,columna,matriz = []):
  for i in range(fila): 
    matriz.append([])
    [matriz[i].append((i,j)) for j in range(columna)]  
  
  for fila in matriz:
    print(fila)
  return matriz

def punto_uno(matriz): # = O(n**2)
  for variable_columna in range(len(matriz[0])):  #O(n**2)
    if variable_columna%2==0:
      for i in range(len(matriz)):
        print(matriz[i][variable_columna])
    else:
      for j in range(len(matriz)-1,-1,-1):
        print(matriz[j][variable_columna])

def punto_uno_luigi(matriz):# = O(n**2)
  n  = len(matriz)
  m = len(matriz[0])
  solucion=[[]for i in range(n+n-1)] #O(n)
  for i in range(n): #O(n**2)
    for j in range(m):
      if j % 2 == 1:
        solucion[j].insert(0,matriz[i][j])
      else:
        solucion[j].append(matriz[i][j])    
  for fila in solucion: # O(n)
    for columna in fila:
      print(columna,end=" ")

def punto_dos(matriz): # = O(n**2)
  if len(matriz) != len(matriz[0]):
    return "matriz no cuadrada"
  n  = len(matriz)
  solucion=[[]for i in range(n+n-1)] #O(n)
  for i in range(n): #O(n**2)
    for j in range(n):
      suma=i+j
      if suma % 2 ==0:
        solucion[suma].insert(0,matriz[i][j])
      else:
        solucion[suma].append(matriz[i][j])    
  for fila in solucion: # O(n)
    for columna in fila:
      print(columna,end=" ")

def punto_uno_recursivo(matriz,variable_colulmna=0,fila=0):
  if variable_colulmna == len(matriz[0]):
    return
  print(matriz[fila][variable_colulmna])
  if variable_colulmna%2 == 0:
    if fila+1 == len(matriz):
      return punto_uno_recursivo(matriz,variable_colulmna+1,fila)
    return punto_uno_recursivo(matriz,variable_colulmna,fila+1)
  else:
    if fila == 0:
      return punto_uno_recursivo(matriz,variable_colulmna+1,fila)
    return punto_uno_recursivo(matriz,variable_colulmna,fila-1)

matriz  = crearMatriz(4,3)
