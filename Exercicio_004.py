# Escreva um programa em Python para encontrar o mínimo e máximo elementos de um dado
# array de tamanho n usando menos que 3n/2 comparações. (Dica: Primeiro, construa um
# grupo de mínimos candidatos e outro de máximos candidatos)

def mergeSort(alist):
  #print("Splitting ",alist)
  if len(alist)>1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    
    mergeSort(lefthalf)
    mergeSort(righthalf)
    
    i=0
    j=0
    k=0
    while i < len(lefthalf) and j < len(righthalf):
      if lefthalf[i] < righthalf[j]:
        alist[k]=lefthalf[i]
        i=i+1
      else:
        alist[k]=righthalf[j]
        j=j+1
      k=k+1
      
    while i < len(lefthalf):
      alist[k]=lefthalf[i]
      i=i+1
      k=k+1
      
    while j < len(righthalf):
      alist[k]=righthalf[j]
      j=j+1
      k=k+1
  return (alist[0],alist[-1])
  
sequence = [1,-2,3,4,5,6,9]
maxMin = mergeSort(sequence)
print ("O Maior é : ", maxMin[1])
print ("O Menor é : ", maxMin[0])
