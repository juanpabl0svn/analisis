#PUNTO 2
def potencia_recursivo(numero,potencia):    #  = O(n^n)
  if potencia == 0:
    return 1
  if potencia == 1:
    return numero
  if potencia < 0:
    return 1/numero * potencia_recursivo(numero,potencia+1)
  return numero * potencia_recursivo(numero,potencia-1)

def potencia_no_recursivo(numero,potencia):      # =  O(n)
  resultado = 1                             #O(1)
  if potencia < 0:                          #O(1)
    for i in range(0,-potencia):            #O(n)
      resultado*=1/numero                   #O(n)
  else:
    for i in range(0,potencia):             #O(n)
      resultado*=numero                     #O(n)
  return resultado

potencia_no_recursivo(3,3)
potencia_recursivo(3,3)

#PUNTO 3
def factorial(numero):    #  = O(n)
  resultado = 1
  for i in range(1,numero+1):
    resultado*=i
  return resultado

def permutaciones(m):     # = O(n)
  return factorial(m)

permutaciones(5)
