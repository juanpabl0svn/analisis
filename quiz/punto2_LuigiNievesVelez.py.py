l=[1,2,3,4,5]
def multiplicacion_recursiva(lista,resultado=1):
    if   len(lista) == 0:
        return resultado 
    resultado *= lista[0]
    return multiplicacion_recursiva(lista[1:],resultado)   

    

def multiplicacion_no_recursiva(lista,resultado=1): #O(n)
    for i in range(len(lista)):
        resultado *= lista.pop()
    return resultado

print(multiplicacion_recursiva(l))
print(multiplicacion_no_recursiva(l))
