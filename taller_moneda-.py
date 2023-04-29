def moneda(l, n, c=[], i=0, r=[]):      #Recursivo
    if sum(c) == n:
        r.append(c)
    elif sum(c) < n and i < len(l):
        moneda(l, n, c +[l[i]] , i, r)
        moneda(l, n, c, i+1, r)
    return r
  
  def moneda(numero,lista,cache=[],respuesta=[]): #No del todo recursivo
    if sum(cache)==numero:
        cache= sorted(cache)
        if cache not in respuesta:
            respuesta.append(cache)
    elif sum(cache)>numero:   
        return 
    for i in range((len(lista))):
        moneda(numero, lista, cache+[lista[i]], respuesta)
    return respuesta
