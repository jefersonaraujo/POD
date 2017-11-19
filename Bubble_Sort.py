def burble_sort(A):
   
    for j in range(len(A)  -1):
        for i in range(len(A) - 1):
                
                if A[i] > A [i+1]:
                    tmp = A[i+1]
                    A[i+1] = A[i]
                    A[i]= tmp
        print (j," : ",A)
    return A

sequence = [9, 8, 2, 1, 6, 5]

burble_sort(sequence)
