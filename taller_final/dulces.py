def caramelos_optimo(caramelos,k,result=0):
  if len(caramelos) <1:
    return result 

  caramelos = sorted(caramelos)
  result+=caramelos.pop(0)

  for i in range(k-1,-1,-1):
    if len(caramelos) != 0:
      caramelos.pop()
  
  
  return caramelos_optimo(caramelos,k,result)
  
def caramelos_no_optimo(caramelos,k,result=0):
  if len(caramelos) ==0:
    return result 

  caramelos = sorted(caramelos)
  result+=caramelos.pop()

  for i in range(k-1,-1,-1):
    if len(caramelos) != 0:
      caramelos.pop(0)
  
  
  return caramelos_no_optimo(caramelos,k,result)

print(caramelos_optimo([1,4,3,2],2))
print('\n')
print(caramelos_no_optimo([1,4,3,2],2))
print('\n')
print(caramelos_optimo([1,5,4,3,2],4))
print('\n')
print(caramelos_no_optimo([5,1,4,3,2],4))


