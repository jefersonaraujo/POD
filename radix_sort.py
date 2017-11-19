import math

def create_buckets(base):
	buckets = []
	for i in range(base):
		buckets.append([])

	return buckets


def radix_sort(items, base):
	tmp = -1
	j = 0
	m = int(math.log(items[0], base)) + 1
	while j < m :
		buckets = create_buckets(base)
		for number in items:
			tmp = number / math.pow(base,j)
			digit = int (tmp % base)
			buckets[digit].append(number)
		a = 0
		for bucket in buckets:
			for i in bucket:
				items[a] = i
				a += 1
			print (buckets)
		j = j + 1


lista = [9, 8, 2, 1, 6, 5]
#Base se for : [10,02,20] é decimal, então a base deve ser 10.
#Base se for :[1000,0010,1111] é binaria, então a base dever ser 2.
radix_sort(lista,10)
