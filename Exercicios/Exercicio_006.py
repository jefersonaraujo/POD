def select_max(array, left, right):
  max_pos = left
  size = len(array) - 1
  i = left
  while i <= right:
    if array[i] > array[max_pos]:
      max_pos = i
    i = i + 1
  return max_pos

def selection_sort(array):
  iteration = 0
  for i in range(len(array) - 1, 0, -1):
    max_pos = select_max(array, 0, i)

    if max_pos != i:
      tmp = array[i]
      array[i] = array[max_pos]
      array[max_pos] = tmp
    iteration = iteration + 1
    print(i, array)
    
sequency = [20, 15, 45, 1, 5, 56, 185]
selection_sort(sequency)