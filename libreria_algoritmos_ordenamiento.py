class SortAlgorithms:
  def bubbleSort(self,lista):
    for i in range(1,len(lista)):
      for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
          lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista
  
  def quickSort(self, lista):
    base = len(lista)
    if base <= 1: return lista
    pivote = lista.pop()
    lista_izquierda , lista_derecha = [],[]
    for elemento in lista:
      if elemento <= pivote:
        lista_izquierda.append(elemento)
      else:
        lista_derecha.append(elemento)
    lista_izquierda,lista_derecha = self.quickSort(lista_izquierda),self.quickSort(lista_derecha)
    return lista_izquierda + [pivote] + lista_derecha
  
  def radixSort(self,lista):
    grande = str(max(lista))
    for i in range(len(lista)):
      string = str(lista[i])
      lista[i] = '0'*(len(grande) - len(string))+string
    for k in range(len(grande)+1):
      dicti = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
      new_list = []
      for i in range(len(lista)):
        digito = str(lista[i])
        dicti[digito[-k]].append(digito)
      for i in dicti.values():
        for j in i:
          new_list.append(j)
      lista = new_list
    return [int(x) for x in lista]
  
  def merge(self,lista_left,lista_right):
    lista_resultado = []
    while lista_left and lista_right:
        if lista_left[0]<lista_right[0]:
            lista_resultado.append(lista_left[0])
            lista_left.pop(0)
        else:
            lista_resultado.append(lista_right[0])
            lista_right.pop(0)
    if lista_left:
        lista_resultado += lista_left
    else:
        lista_resultado += lista_right
    return lista_resultado
  
  def mergeSort(self,lista):
    base = len(lista)
    if base <= 1:
        return lista
    lista_izquierda = lista[:base//2]
    lista_derecha = lista[base//2:]
        
    lista_izquierda = self.mergeSort(lista_izquierda)
    lista_derecha = self.mergeSort(lista_derecha)
    
    return self.merge(lista_izquierda,lista_derecha)
  
  def heapify(self, array, tamaño, indice_raiz):

    raiz = indice_raiz

    hijo_izquierdo = 2 * indice_raiz + 1
    hijo_derecho = 2 * indice_raiz + 2

    if hijo_izquierdo < tamaño and array[hijo_izquierdo] > array[raiz]:
        raiz = hijo_izquierdo

    if hijo_derecho < tamaño and array[hijo_derecho] > array[raiz]:
        raiz = hijo_derecho

    if raiz != indice_raiz:
        array[indice_raiz], array[raiz] = array[raiz], array[indice_raiz]
        self.heapify(array, tamaño, raiz)

  def heapSort(self,array):

    tamaño = len(array)

    for indice_raiz in range((tamaño // 2) - 1, -1, -1):
        self.heapify(array, tamaño, indice_raiz)

    for ultimo_indice in range(tamaño - 1, 0, -1):
        array[0], array[ultimo_indice] = array[ultimo_indice], array[0]
        self.heapify(array, ultimo_indice, 0)

    return array
  
  def countingSort(self,lista):
    tamaño = len(lista)
    new_lista = [0] * tamaño

    valor_max = max(lista) + 1
    contar = [0] * valor_max

    for i in range(0, tamaño):
        contar[lista[i]] += 1

    for i in range(1, valor_max):
        contar[i] += contar[i - 1]

    for i in range(tamaño - 1, -1, -1):
        new_lista[contar[lista[i]] - 1] = lista[i]
        contar[lista[i]] -= 1

    return new_lista


orden = SortAlgorithms()

print('Burbuja')
print(orden.bubbleSort([4,2,1,5,2,3]))
print('\nQuick Sort')
print(orden.quickSort([4,2,1,5,2,3]))
print('\nMerge Sort')
print(orden.mergeSort([4,2,1,5,2,3]))
print('\nMerge Sort')
print(orden.radixSort([4,2,1,5,2,3]))
print('\nHeap Sort')
print(orden.heapSort([4,2,1,5,2,3]))
print('\nCounting Sort')
print(orden.countingSort([4,2,1,5,2,3]))
