def sort(alist):
    size = len(alist)
    for i in range(1, size):
        current = alist[i]
        j = i

        while j > 0 and alist[j-1] > current:
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = current

array = [55, 33, 25, 2, 3, 45, 99, 4, 14, 20, 30]
sort(array)
print(array)