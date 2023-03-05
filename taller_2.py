from math import factorial as factorial

class Conteo:

  def combinaciones_repite(self,m,n):
    if m<n:
      return "Error"
    numerador = factorial(m + n -1)
    denominador = factorial(n)*factorial(m-1)
    return numerador/denominador

  def combinaciones_no_repite(self,m,n):
    if m<n:
      return "Error"
    numerador = factorial(m)
    denominador = factorial(n)*factorial(m - n)
    return numerador/denominador

  def variacion_no_repite(self,m,n):
    if m<n:
      return "Error"
    numerador = factorial(m)
    denominador = factorial(m - n)
    return numerador/denominador
  
  def variacion_repite(self,m):
    if m<n:
      return "Error"
    return m**n
  
  def permutacion_no_repite(self,m):
    return factorial(m)

  def permutacion_repite(self,p,lista:list):
    denominador = 1
    for denminador in lista:
      denominador *= factorial(denminador)
    return p/denominador
  
  def variacion_no_repite_especial_or(self,m,n):
    if m<n:
      return "Error"
    numerador = factorial(m)
    valor = 0
    for numero in range(n):
      denominador = factorial(m - numero) 
      valor+= numerador/denominador
    return valor
  
  def variacion__no_repite_especial_and(self,m:int,n:int,se_repite):
    if m<n:
      return "Error"
    numerador = factorial(m)
    valor = 0
    for numero in range(n):
      denominador = factorial(m - numero) 
      valor*= numerador/denominador
    return valor
