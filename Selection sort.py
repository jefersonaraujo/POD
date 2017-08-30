
def select_max(A,left, right):
    max_pos = left

    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i

        i = i + 1
    return max_pos


def selection_sort(A):
    for i in range(len(A) -1, 0, -1): # pega o tamanho de 'A' da ultima posicao até o 0 ; e descrementa 
        max_pos = select_max(A, 0, i)


        if max_pos !=i:
            tmp = A[i]
            A[i] = A[max_pos]
            A[max_pos] = tmp

        print(i, A)


sequence = [13,11,4,7,8,2]

selection_sort(sequence)
