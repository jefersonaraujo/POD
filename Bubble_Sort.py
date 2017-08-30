def burble_sort(A):
    n = len(A)

    for j in range(len(A)  -1):
        for i in range(len(A) - 1):
                if A[i] > A [i+1]:
                    tmp = A[i+1]
                    A[i+1] = A[i]
                    A[i]= tmp
        print (A)
    return A

sequence = [13,11,4,7,8,2]
burble_sort(sequence)
