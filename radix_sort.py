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


lista = [223,456,123,789,113]
radix_sort(lista,10)