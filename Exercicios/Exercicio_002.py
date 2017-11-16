# Escreva uma classe em Python contendo um método que recebe dois arrays (de tamanho n)a e b contendo valores inteiros e calcula o produto de a por b. Sendo assim, seu métododeve retornar um novo array c, tal que c[i] = a[i] * b[i], para i = 0, ..., n-1. Faça o estudocomparativo em uma tabela e gráfico do desempenho de seu código.

# class GenerationList(object):

def listGeneration(listA,listB):
	listC =[]
	
	for i in range(len(listA)):
		for j in range(len(listB ) ):		 
			listC.append(listA[i] * listB[j])
		return listC



sequence = [2,2,5,9]
sequence2 = [3,2,4,2,6]

print (listGeneration(sequence,sequence2))

# obj = GenerationList()
# obj.listGeneration(sequence,sequence2)
       
